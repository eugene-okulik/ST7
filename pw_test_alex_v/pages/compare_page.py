from selenium.webdriver.common.by import By

from ui_test_alex_v.pages.base_page import BasePage


class ComparePage(BasePage):

    def compared_product_title_displayed_is(self, test_product_title):

        prodict_title = self.find((By.CLASS_NAME, 'product-item-name')).text
        return prodict_title == test_product_title
