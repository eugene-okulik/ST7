import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import AccountLocators as loc


class GearPage(BasePage):
    page_url = '/gear.html'

    @allure.step('Checking teh Gear page title')
    def correct_redirect(self):
        assert self.find(loc.HEADER).is_displayed
        assert self.find(loc.HEADER).text == 'Gear'

    @allure.step('Checking finding the bottle')
    def bottle_icon(self):
        bottle = self.find(loc.BOTTLE_ICON)
        self.actions_move_to_element(bottle)

    @allure.step('Checking adding the bottle to the cart')
    def add_to_cart(self):
        self.find(loc.ADD_TO_CART_ICON).click()

    @allure.step('Checking if the cart number is correct')
    def check_cart_number(self):
        assert self.find(loc.CART_NUMBER).is_displayed
