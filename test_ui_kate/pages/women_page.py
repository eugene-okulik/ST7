import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import Locators as loc


class WomenPage(BasePage):
    page_url = '/women/tops-women/tanks-women.html'

    @allure.step('Checking the page title')
    def check_page_title(self, text):
        assert self.find_element(loc.HEADER).text == text
