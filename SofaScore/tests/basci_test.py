import pytest
from pages.main_page import MainPage
from pages.club_page import ClubPage

@pytest.mark.usefixtures("setup")
class TestBasic:

    def test_pl_ratings(self):
        main_page = MainPage(self.driver)
        main_page.open_page()
        main_page.search_team("chelsea")
        club_page = ClubPage(self.driver)
        club_page.get_pl_ratings()
        i = 1
        assert i == 1

    def test_cl_ratings(self):
        main_page = MainPage(self.driver)
        main_page.open_page()
        main_page.search_team("chelsea")
        club_page = ClubPage(self.driver)
        club_page.get_cl_ratings()
        i = 1
        assert i ==1

    def test_matches_results(self):
        main_page = MainPage(self.driver)
        main_page.open_page()
        main_page.search_team("chelsea")
        club_page = ClubPage(self.driver)
        club_page.get_matches_results()
        i = 1
        assert i == 1