import allure
from selenium.webdriver.common.by import By
from ui_tests_yevdokiienko.pages.base_page import BasePage
from ui_tests_yevdokiienko.pages.locators import CartLocators as loc
from selenium.webdriver.common.action_chains import ActionChains


class EcoFriendlyCollectionPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    @allure.step('Account page')
    def click_product(self, product_number):
        self.find((By.XPATH, f'{loc.PRODUCT}[{product_number}]')).click()

    def add_to_compare(self, product_number):
        product = self.find((By.XPATH, f'{loc.PRODUCT}[{product_number}]'))
        add_to_compare_button = self.find((By.XPATH, f'{loc.ADD_TO_COMPARE}[{product_number}]'))
        actions = ActionChains(self.driver)
        actions.move_to_element(product)
        actions.click(add_to_compare_button)
        actions.perform()

    def check_compare_products(self, product_name):
        assert product_name in self.find(loc.COMPARE_PRODUCTS).text

    def add_to_wish_list(self, product_number):
        product = self.find((By.XPATH, f'{loc.PRODUCT}[{product_number}]'))
        add_to_wish_list_button = self.find((By.XPATH, f'{loc.ADD_TO_WISH_LIST}[{product_number}]'))
        actions = ActionChains(self.driver)
        actions.move_to_element(product)
        actions.click(add_to_wish_list_button)
        actions.perform()
