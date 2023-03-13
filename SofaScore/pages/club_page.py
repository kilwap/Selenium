import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import locators


class ClubPage:

    def __init__(self, driver):
        self.logger = logging.getLogger(__name__)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.team_info_box = locators.ClubPage.team_info_box
        self.top_players_box = locators.ClubPage.top_players_box
        self.players_ratings = locators.ClubPage.players_ratings
        self.competition_select_button = locators.ClubPage.competition_select_button
        self.champions_league_button = locators.ClubPage.champions_league_button
        self.premier_league_button = locators.ClubPage.premier_league_button
        self.match_info_close_button = locators.ClubPage.match_info_close_button
        self.home_team_name = locators.ClubPage.home_team_name
        self.away_team_name = locators.ClubPage.away_team_name
        self.home_team_goals = locators.ClubPage.homea_team_goals
        self.away_team_goals = locators.ClubPage.away_team_goals

    def get_pl_ratings(self, number_of_players=3):
        self.logger.info("getting rating of " + str(number_of_players) + " best players in Premier League")
        info_box = self.wait.until(EC.presence_of_element_located((self.team_info_box)))
        ActionChains(self.driver).scroll_to_element(info_box).perform()
        ratings = self.wait.until(EC.presence_of_element_located((self.top_players_box)))
        ActionChains(self.driver).scroll_to_element(ratings).perform()
        self.driver.find_element(*self.competition_select_button).click()
        self.wait.until(EC.presence_of_element_located((self.premier_league_button))).click()
        best_players = self.wait.until(EC.presence_of_all_elements_located((self.players_ratings)))
        print("Top 3 players in premier league:")
        i = 1
        for player in best_players:
            player_name = player.find_element(By.TAG_NAME, "img").get_attribute("alt")
            player_rating = player.find_element(By.CLASS_NAME, "geIsJJ").text
            player_position = (player.find_element(By.CLASS_NAME, "dRAnTt").text)
            print(player_position + ". " + player_name + " " + player_rating)
            if i == number_of_players:
                break
            i += 1

    def get_cl_ratings(self, number_of_players=3):
        self.logger.info("getting rating of " + str(number_of_players) + " best players in Champions League")
        info_box = self.wait.until(EC.presence_of_element_located((self.team_info_box)))
        ActionChains(self.driver).scroll_to_element(info_box).perform()
        ratings = self.wait.until(EC.presence_of_element_located((self.top_players_box)))
        ActionChains(self.driver).scroll_to_element(ratings).perform()
        self.driver.find_element(*self.competition_select_button).click()
        self.wait.until(EC.presence_of_element_located((self.champions_league_button))).click()
        best_players = self.wait.until(EC.presence_of_all_elements_located((self.players_ratings)))
        print("Top 3 players in premier league:")
        i = 1
        for player in best_players:
            player_name = player.find_element(By.TAG_NAME, "img").get_attribute("alt")
            player_rating = player.find_element(By.CLASS_NAME, "geIsJJ").text
            player_position = (player.find_element(By.CLASS_NAME, "dRAnTt").text)
            print(player_position + ". " + player_name + " " + player_rating)
            if i == number_of_players:
                break
            i += 1

    def get_matches_results(self):
        self.logger.info("Getting result of matches")
        info_box = self.wait.until(EC.presence_of_element_located((self.team_info_box)))
        ActionChains(self.driver).scroll_to_element(info_box).perform()
        ratings = self.wait.until(EC.presence_of_element_located((self.top_players_box)))
        ActionChains(self.driver).scroll_to_element(ratings).perform()
        self.wait.until(EC.presence_of_element_located((self.match_info_close_button))).click()
        print("matches results: ")
        i=1
        while i < 4:
            match = self.driver.find_element(By.XPATH,
                                        "//div[@class='sc-hLBbgP sYIUR']//div[@class='sc-hLBbgP gnEaMj']/a[" + str(
                                            i) + "]")
            match.click()
            home_team = self.wait.until(EC.presence_of_element_located((self.home_team_name)))
            away_team = self.driver.find_element(*self.away_team_name)
            home_goals = self.driver.find_element(*self.home_team_goals)
            away_goals = self.driver.find_element(*self.away_team_goals)
            print(home_team.text + " " + home_goals.text + " - " + away_goals.text + " " + away_team.text)
            self.driver.find_element(*self.match_info_close_button).click()
            i += 1