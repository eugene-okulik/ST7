import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from ui_test_alex_v.pages.base_page import BasePage


class EcoPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def sort_products_by_name(self):
        sort_dropdown = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "select#sorter"))
        )
        sort_dropdown.click()
        sort_by_name_option = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//option[@value='name']"))
        )
        sort_by_name_option.click()
        WebDriverWait(self.driver, 10).until(
            ec.text_to_be_present_in_element((By.CSS_SELECTOR, "select#sorter option[selected='selected']"),
                                             "Product Name")
        )
        product_names = self.driver.find_elements(By.CSS_SELECTOR, ".product-item-name a")
        names = [name.text for name in product_names]

        return names == sorted(names)

    def choose_product(self):
        product_elements = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//a[@class='product-item-link']"))
        )

        if not product_elements:
            raise Exception("No products found on the page")

        random_product = random.choice(product_elements)
        random_product.click()
