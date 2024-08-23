import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import Locators as loc


class GearPage(BasePage):
    page_url = '/gear.html'

    @allure.step('Checking the Gear page title')
    def check_correct_redirect(self, text):
        assert self.find(loc.HEADER).text == text

    @allure.step('Checking if the cart number is correct')
    def check_number_items_in_cart(self, number):
        assert self.find(loc.CART_NUMBER).text == number
