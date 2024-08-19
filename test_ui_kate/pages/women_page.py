import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import AccountLocators as loc


class WomenPage(BasePage):
    page_url = '/women/tops-women/tanks-women.html'

    @allure.step('Checking the page title')
    def page_title(self):
        assert self.find(loc.HEADER).text == 'Bras & Tanks'
