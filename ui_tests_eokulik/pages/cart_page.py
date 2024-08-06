from ui_tests_eokulik.pages.base_page import BasePage
from ui_tests_eokulik.pages.locators import CartLocators as loc


# PRODUCT_ROW = (By.CSS_SELECTOR, 'tr[class="success"]')


class CartPage(BasePage):
    page_url = '/cart.html'

    def check_product_in_cart(self, product_name):
        assert product_name in self.find(loc.PRODUCT_ROW).text
