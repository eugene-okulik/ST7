import allure
from playwright.sync_api import expect
from pw_tests_yevdokiienko.pages.base_page import BasePage
from pw_tests_yevdokiienko.pages.locators import SaleLocators as loc


class MenDealPage(BasePage):
    page_url = '/promotions/men-sale.html'

    @allure.step('Men deal page')
    def check_men_page_opened(self, page_title):
        expect(self.find(loc.MEN_PAGE_TITLE)).to_contain_text(page_title)

