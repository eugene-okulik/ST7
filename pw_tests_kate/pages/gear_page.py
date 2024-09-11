import allure
from pw_tests_kate.pages.base_page import BasePage
from pw_tests_kate.pages.locators import Locators as loc
from playwright.sync_api import expect


class GearPage(BasePage):
    page_url = '/gear.html'

    @allure.step('Adding a bottle item to cart')
    def add_bottle_to_cart(self):
        self.move_to_element(loc.BOTTLE_ICON)
        self.find_and_click_element(loc.ADD_TO_CART_ICON)

    @allure.step('Checking if the cart number is correct')
    def check_number_items_in_cart(self, number):
        expect(self.find_element_by_locator(loc.CART_NUMBER)).to_have_text(number)
