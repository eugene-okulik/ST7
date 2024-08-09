import allure
from ui_tests_yevdokiienko.pages.base_page import BasePage
from ui_tests_yevdokiienko.pages.locators import SaleLocators as loc


class WomenDealPage(BasePage):
    page_url = '/promotions/women-sale.html'

    @allure.step('Women deal page')
    def check_women_page_opened(self, page_title):
        assert page_title in self.find(loc.WOMEN_PAGE_TITLE).text
