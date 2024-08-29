from playwright.sync_api import expect
from pw_tests_yevdokiienko.pages.base_page import BasePage
from pw_tests_yevdokiienko.pages.locators import CartLocators as loc


class CartPage(BasePage):
    page_url = None

    def check_product_in_cart(self, product_name):
        expect(self.find(loc.PRODUCT_IN_CARD)).to_contain_text(product_name)

    def check_price_in_cart(self, product_price):
        expect(self.find(loc.PRODUCT_PRICE_IN_CARD)).to_contain_text(product_price)
