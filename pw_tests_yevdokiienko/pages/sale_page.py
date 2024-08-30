import allure
from playwright.sync_api import expect
from pw_tests_yevdokiienko.pages.base_page import BasePage
from pw_tests_yevdokiienko.pages.locators import SaleLocators as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    @allure.step('Sale page')
    def check_sale_page_able(self, sale):
        expect(self.find(loc.SALE_VERIFY_PAGE)).to_contain_text(sale)

    def click_women_deals(self):
        self.find(loc.WOMEN_DEALS).click()

    def click_men_deals(self):
        self.find(loc.MEN_DEALS).click()

    def verify_percent_of_sale(self, sale):
        expect(self.find(loc.VERIFY_OFF)).to_contain_text(sale)
