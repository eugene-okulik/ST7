import allure
from playwright.sync_api import expect
from pw_tests_yevdokiienko.pages.base_page import BasePage
from pw_tests_yevdokiienko.pages.locators import SaleLocators as loc


class WomenDealPage(BasePage):
    page_url = '/promotions/women-sale.html'

    @allure.step('Women deal page')
    def check_women_page_opened(self, page_title):
        expect(self.find(loc.WOMEN_PAGE_TITLE)).to_contain_text(page_title)
