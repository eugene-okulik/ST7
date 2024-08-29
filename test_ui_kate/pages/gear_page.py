import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import Locators as loc


class GearPage(BasePage):
    page_url = '/gear.html'

    @allure.step('Checking the Gear page title')
    def check_redirect_is_correct(self):
        assert self.find_element(loc.HEADER).text == 'Gear'

    @allure.step('Adding a bottle item to cart')
    def add_bottle_to_cart(self):
        self.find_and_hover_element(loc.BOTTLE_ICON)
        self.find_and_click_element(loc.ADD_TO_CART_ICON)

    @allure.step('Checking if the cart number is correct')
    def check_number_items_in_cart(self, number):
        assert self.find_element(loc.CART_NUMBER).text == number
