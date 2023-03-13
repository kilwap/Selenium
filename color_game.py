import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.implicitly_wait(5)

driver.get("http://flashbynight.com/drench/")
driver.maximize_window()

RED_COLOR = (255, 0, 0, 255)
LIGHT_COLOR = (204, 255, 204, 255)
PURPLE_COLOR = (116, 62, 244, 255)
PINK_COLOR = (255, 159, 255, 255)
GREEN_COLOR = (102, 204, 0, 255)
YELLOW_COLOR = (255, 204, 0, 255)

GREEN = "b1"
PINK = "b2"
PURPLE = "b3"
LIGHT = "b4"
RED = "b5"
YELLOW = "b6"


def print_grid(grid):
    for i in range(14):
        for j in range(14):
            print("%s " % grid[j][i], end="")
        print(" ")


def get_moves(driver):
    webElement = driver.find_element(By.CLASS_NAME, "moveNum")
    return int(webElement.text)


def click_button(driver, color):
    driver.find_element(By.ID, color).click()


def get_grid(driver):
    webElement = driver.find_element(By.ID, "canvasholder")
    webElement.screenshot("div.png")


def process_grid():
    im = Image.open("div.png")
    pix = im.load()
    cell_size = im.size[1] / 14
    start_point = 1 + cell_size / 2
    grid = [[None for x in range(14)] for y in range(14)]

    for i in range(14):
        for j in range(14):
            across = start_point + j * cell_size
            down = start_point + i * cell_size

            color = pix[across, down]

            if color == RED_COLOR:
                grid[j][i] = RED
            elif color == LIGHT_COLOR:
                grid[j][i] = LIGHT
            elif color == PURPLE_COLOR:
                grid[j][i] = PURPLE
            elif color == PINK_COLOR:
                grid[j][i] = PINK
            elif color == GREEN_COLOR:
                grid[j][i] = GREEN
            elif color == YELLOW_COLOR:
                grid[j][i] = YELLOW
            else:
                print("NO MATCH!")
                raise Exception("Failed to match")

            pix[across, down] = (0, 0, 0, 255)
    return grid, im


def _str_it(x, y):
    return "(%s,%s)" % (x, y)

def calc_v1(grid):
    seen = [_str_it(0, 0)]
    primary = grid[0][0]

    results = {
        "b1": 0,
        "b2": 0,
        "b3": 0,
        "b4": 0,
        "b5": 0,
        "b6": 0
    }

    _view_coord(grid, primary, seen, 0, 0, results)

    return results


def _view_coord(grid, primary, seen, x, y, results):
    if x < 13:
        _process_neighbour(grid, primary, seen, x+1, y, results)
    if x > 0:
        _process_neighbour(grid, primary, seen, x-1, y, results)
    if y < 13:
        _process_neighbour(grid, primary, seen, x, y+1, results)
    if y > 0:
        _process_neighbour(grid, primary, seen, x, y-1, results)


def _process_neighbour(grid, primary, seen, x, y, results):
    target = _str_it(x, y)
    if target not in seen:
        seen.append(target)
        if grid[y][x] == primary:
            _view_coord(grid, primary, seen, x, y, results)
        else:
            results[grid[y][x]] += 1


playing = True

while playing:
    if get_moves(driver) > 0:
        get_grid(driver)

        try:
            grid, im = process_grid()
            move_options = calc_v1(grid)

            found_max = 0
            maxes = []

            for key, val in move_options.items():
                if val > found_max:
                    found_max = val
                    maxes = [key]
                elif val == found_max:
                    maxes.append(key)

            if found_max == 0:
                print("No options!")

            choice = random.choice(maxes)
            click_button(driver, choice)
        except Exception:
            if get_moves(driver) > 0:
                driver.find_element(By.ID, "canvasholder").click()
                continue
            print("Stop due to an error ? roud over?")
            playing = False
    else:
        print("Stopped - out of moves!")
        playing = False

    time.sleep(.5)