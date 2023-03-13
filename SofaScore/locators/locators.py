from selenium.webdriver.common.by import By


class MainPage:
    cookies_accept_button = (By.XPATH, "/html/body/div[4]/div[2]/div[1]/div[2]/div[2]/button[1]")
    search_input = (By.XPATH, "//*[@id='__next']/div/header/div[1]/div/div[2]/div/form/input")
    first_result_link = (By.XPATH, "//*[@id='__next']/div/header/div[1]/div/div[2]/div/div/div/div[1]/div[1]/a/div")


class ClubPage:
    team_info_box = (By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[1]")
    top_players_box = (By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]")
    players_ratings = (By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/a")
    competition_select_button = (By.ID, "downshift-7-toggle-button")
    champions_league_button = (By.ID, "downshift-7-item-1")
    premier_league_button = (By.ID, "downshift-7-item-0")
    match_info_close_button = (By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[2]/button")
    home_team_name = (By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/span")
    away_team_name = (By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/span")
    homea_team_goals = (By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/span")
    away_team_goals = (By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[3]/span")