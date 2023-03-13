import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# setting up driver with setings
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
# driver.implicitly_wait(10)   proboje przerobic na explicit
wait = WebDriverWait(driver, 10)
# opening website
driver.get("https://www.sofascore.com/")
driver.maximize_window()

# accepting cookies

wait.until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div[1]/div[2]/div[2]/button[1]"))
).click()


# searching team
driver.find_element(By.XPATH, "//*[@id='__next']/div/header/div[1]/div/div[2]/div/form/input").send_keys("chelsea")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/header/div[1]/div/div[2]/div/div/div/div[1]/div[1]/a/div"))
).click()
info_box = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[1]")))
ActionChains(driver).scroll_to_element(info_box).perform()

ratings = wait.until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]"))
)
ActionChains(driver).scroll_to_element(ratings).perform()
rating_table = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/a"))
)

print("Top 3 players in premier league:")
i=0
for player in rating_table:
    player_name = player.find_element(By.TAG_NAME, "img").get_attribute("alt")
    player_rating = player.find_element(By.CLASS_NAME, "geIsJJ").text
    player_position = (player.find_element(By.CLASS_NAME, "dRAnTt").text)
    print(player_position + ". " + player_name + " " + player_rating)
    if i == 2:
        break
    i += 1

driver.find_element(By.ID, "downshift-12-toggle-button").click()
wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#downshift-12-item-1"))
).click()

# this below closes window nex to matches
wait.until(EC.presence_of_element_located((By.XPATH,
                    "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[2]/button"))).click()

rating_table = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/a")))
print("Top 3 players in champions league")
i=0
for player in rating_table:
    player_name = player.find_element(By.TAG_NAME, "img").get_attribute("alt")
    player_rating = player.find_element(By.CLASS_NAME, "geIsJJ").text
    player_position = (player.find_element(By.CLASS_NAME, "dRAnTt").text)
    print(player_position + ". " + player_name + " " + player_rating)
    if i == 2:
        break
    i += 1

i = 1  # z jakiegos powodu find elements nie dzialalo wiec mam takie obejscie
print("last 3 matches: ")
while i < 4:
    match = driver.find_element(By.XPATH, "//div[@class='sc-hLBbgP sYIUR']//div[@class='sc-hLBbgP gnEaMj']/a["+str(i)+"]")
    match.click()
    home_team = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/span")))
    away_team = driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/span")
    home_goals = driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/span")
    away_goals = driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[3]/span")
    print(home_team.text + " " + home_goals.text + " - " + away_goals.text + " " + away_team.text)
    driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[2]/button").click()
    i += 1
