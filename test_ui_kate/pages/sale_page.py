import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import AccountLocators as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    @allure.step('Checking the Gear link')
    def gear_page(self):
        self.find(loc.GEAR_LINK).click()

    @allure.step('Checking redirect to Bras and Tanks')
    def bras_and_tops(self):
        self.find(loc.BRAS_AND_TANKS_LINK).click()
