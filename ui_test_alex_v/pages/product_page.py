from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from ui_test_alex_v.pages.base_page import BasePage


class ProductPage(BasePage):
    def add_to_compare_product(self):
        add_to_compare = self.find((By.XPATH, "//div[@class='product-addto-links']/a[2]"))
        add_to_compare.click()

    def add_to_wish_list(self):
        add_to_wishlist = self.find((By.XPATH, "//div[@class='product-addto-links']/a[1]"))
        add_to_wishlist.click()

    def go_to_comparison_list(self):
        comparison_list_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.LINK_TEXT, 'comparison list')))
        comparison_list_button.click()

    def get_product_title(self):
        product_title = self.find((By.XPATH, "//span[@class='base']")).text
        return product_title
