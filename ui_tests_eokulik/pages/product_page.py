import allure
from selenium.webdriver.common.by import By
from ui_tests_eokulik.pages.base_page import BasePage


class ProductPage(BasePage):

    @allure.step('Open product page')
    def open(self, product_id):
        self.driver.get(f'https://www.demoblaze.com/prod.html?idp_={product_id}')

    @allure.step('Check button is displayed')
    def check_add_to_cart_button(self, product_id):
        assert self.find(
            self.add_to_cart_button(product_id)
        ).is_displayed(), 'Add to cart button is not displayed'

    def click_add_to_cart(self, product_id):
        self.find(self.add_to_cart_button(product_id)).click()

    @staticmethod
    def add_to_cart_button(product_id):
        return By.CSS_SELECTOR, f'[onclick="addToCart({product_id})"]'
