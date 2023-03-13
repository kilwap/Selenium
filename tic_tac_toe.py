import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# setting webdriver with options, that the browser will stay open after script
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("window-size=600,600")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
driver.implicitly_wait(5)

# opening site
driver.get("https://playtictactoe.org/")
# driver.maximize_window()

# accepting cookies
driver.find_element("id", "consent").click()

# settings all fields as var
top_left = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square top left']")
top_left_status = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square top left']/div")
top_middle = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square top']")
top_middle_status = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square top']/div")
top_right = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square top right']")
top_right_status = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square top right']/div")
left = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square left']")
left_status = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square left']/div")
middle = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square']")
middle_status = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square']/div")
right = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square right']")
right_status = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square right']/div")
bottom_left = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square bottom left']")
bottom_left_status = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square bottom left']/div")
bottom_middle = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square bottom']")
bottom_middle_status = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square bottom']/div")
bottom_right = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square bottom right']")
bottom_right_status = driver.find_element("xpath", "//div[@class='game']/div[@class='board']/div[@class='square bottom right']/div")

# function that analyze the board ane chose the best possible move right now
def make_move():
    board = {
        "row_1": [[top_left_status.get_attribute("class"), top_middle_status.get_attribute("class"), top_right_status.get_attribute("class")],
                  [top_left, top_middle, top_right]],
        "row_2": [[left_status.get_attribute("class"), middle_status.get_attribute("class"), right_status.get_attribute("class")],
                  [left, middle, right]],
        "row_3": [[bottom_left_status.get_attribute("class"), bottom_middle_status.get_attribute("class"), bottom_right_status.get_attribute("class")],
                  [bottom_left, bottom_middle, bottom_right]],
        "column_1": [[top_left_status.get_attribute("class"), left_status.get_attribute("class"), bottom_left_status.get_attribute("class")],
                     [top_left, left, bottom_left]],
        "column_2": [[top_middle_status.get_attribute("class"), middle_status.get_attribute("class"), bottom_middle_status.get_attribute("class")],
                     [top_middle, middle, bottom_middle]],
        "column_3": [[top_right_status.get_attribute("class"),right_status.get_attribute("class"), bottom_right_status.get_attribute("class")],
                     [top_right, right, bottom_right]],
        "diagonal_1": [[top_left_status.get_attribute("class"), middle_status.get_attribute("class"), bottom_right_status.get_attribute("class")],
                       [top_left, middle, bottom_right]],
        "diagonal_2": [[bottom_left_status.get_attribute("class"), middle_status.get_attribute("class"), top_right_status.get_attribute("class")],
                       [bottom_left, middle, top_right]]
    }
    # check if possible to win in this move
    for key in board.keys():
        if board[key][0].count("x") > 1:
            for i in range(3):
                if board[key][0][i] == "":
                    board[key][1][i].click()
                    return

    # check if rival can win and try to stop him
    for key in board.keys():
        if board[key][0].count("o") > 1:
            for i in range(3):
                if board[key][0][i] == "":
                    board[key][1][i].click()
                    return

    # if no one is close to win make other move
    important_fields = {
        "bottom_left_corner": [bottom_left_status.get_attribute("class"), bottom_left],
        "middle_cell": [middle_status.get_attribute("class"), middle],
        "top_left_corner": [top_left_status.get_attribute("class"), top_left],
        "bottom_right_corner": [bottom_right_status.get_attribute("class"), bottom_right],
        "top_right_corner": [top_right_status.get_attribute("class"), top_right],
        "top_middle_cell": [top_middle_status.get_attribute("class"), top_middle],
        "bottom_middle_cell": [bottom_middle_status.get_attribute("class"), bottom_middle],
        "left_middle_cell": [left_status.get_attribute("class"), left],
        "right_middle_cell": [right_status.get_attribute("class"), right]
    }
    for key in important_fields.keys():
        if important_fields[key][0] == "":
            important_fields[key][1].click()

# function that makes moves until round is finished
def play_round():
    while driver.find_element("xpath", "//div[@class='game']/div[@class='restart']").get_attribute("style") == "display: none;":
        print("wykonuję ruch")
        make_move()
        time.sleep(1)

# loop that plays game until player wins 3 times
player_wins = driver.find_element("xpath", "//div[@class='scores p1']//span[@class='score']").text
while player_wins < "3":
    play_round()
    print(player_wins)
    driver.find_element("xpath", "//div[@class='game']/div[@class='restart']").click()
    player_wins = driver.find_element("xpath", "//div[@class='scores p1']//span[@class='score']").text


