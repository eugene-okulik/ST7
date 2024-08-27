import allure
from playwright.sync_api import expect
from pw_tests_eokulik.pages.base_page import BasePage


class ProductPage(BasePage):

    @allure.step('Open product page')
    def open(self, product_id):
        self.page.goto(f'https://www.demoblaze.com/prod.html?idp_={product_id}')

    @allure.step('Check button is displayed')
    def check_add_to_cart_button(self, product_id):
        expect(self.find(self.add_to_cart_button(product_id))).to_be_visible()

    def click_add_to_cart(self, product_id):
        self.find(self.add_to_cart_button(product_id)).click()
        # self.page.wait_for_event('dialog')

    @staticmethod
    def add_to_cart_button(product_id):
        return f'[onclick="addToCart({product_id})"]'
