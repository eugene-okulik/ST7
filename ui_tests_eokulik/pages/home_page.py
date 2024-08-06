import allure
from selenium.webdriver.common.by import By
from ui_tests_eokulik.pages.base_page import BasePage


class HomePage(BasePage):
    page_url = '/index.html'

    @allure.step('Click product')
    def click_product(self, product_name):
        self.find((By.LINK_TEXT, product_name)).click()
