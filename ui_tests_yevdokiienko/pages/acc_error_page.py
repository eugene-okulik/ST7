import allure
from ui_tests_yevdokiienko.pages.base_page import BasePage
from ui_tests_yevdokiienko.pages.locators import CartLocators as loc


class AccountErrorPage(BasePage):
    page_url = None

    @allure.step('Add to wish list without registration')
    def add_to_wish_list_failed(self, error_massage):
        assert error_massage in self.find(loc.WISH_LIST_ERROR).text
