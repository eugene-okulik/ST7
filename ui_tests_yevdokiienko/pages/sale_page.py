import allure
from ui_tests_yevdokiienko.pages.base_page import BasePage
from ui_tests_yevdokiienko.pages.locators import SaleLocators as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    @allure.step('Sale page')
    def check_sale_page_able(self, sale):
        assert sale in self.find(loc.SALE_VERIFY_PAGE).text

    def click_women_deals(self):
        self.find(loc.WOMEN_DEALS).click()

    def click_men_deals(self):
        self.find(loc.MEN_DEALS).click()

    def verify_percent_of_sale(self, sale):
        assert sale in self.find(loc.VERIFY_OFF).text
