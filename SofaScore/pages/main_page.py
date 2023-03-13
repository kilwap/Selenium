from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import locators
import logging


class MainPage:

    def __init__(self, driver):
        self.logger = logging.getLogger(__name__)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.cookie_accept_button = locators.MainPage.cookies_accept_button
        self.search_input = locators.MainPage.search_input
        self.first_result = locators.MainPage.first_result_link

    def open_page(self):
        self.logger.info("Openig page")
        self.driver.get("https://www.sofascore.com/")
        self.wait.until(EC.presence_of_element_located((self.cookie_accept_button))).click()

    def search_team(self, team):
        self.logger.info("searching team")
        self.wait.until(EC.presence_of_element_located((self.search_input))).send_keys(team)
        self.wait.until(EC.presence_of_element_located((self.first_result))).click()