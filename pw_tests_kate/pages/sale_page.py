import allure
from pw_tests_kate.pages.base_page import BasePage
from pw_tests_kate.pages.locators import Locators as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    @allure.step('Checking if the link redirects to the Luma Gear page')
    def click_luma_gear_link(self):
        self.find_and_click_element(loc.LUMA_GEAR_LINK)

    @allure.step('Checking if the link redirects to the Bras and Tanks page')
    def click_bras_and_tanks_link(self):
        self.find_and_click_element(loc.BRAS_AND_TANKS_LINK)
