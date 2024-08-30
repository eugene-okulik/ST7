import allure
from playwright.sync_api import expect
from pw_tests_yevdokiienko.pages.base_page import BasePage
from pw_tests_yevdokiienko.pages.locators import CartLocators as loc


class EcoFriendlyCollectionPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    @allure.step('Account page')
    def click_product(self, product_number):
        self.find(f'{loc.PRODUCT}[{product_number}]').click()

    def add_to_compare(self, product_number):
        add_to_compare_button = self.find(f'{loc.ADD_TO_COMPARE}[{product_number}]')
        add_to_compare_button.click()

    def check_compare_products(self, product_name):
        expect(self.find(loc.COMPARE_PRODUCTS)).to_contain_text(product_name)

    def add_to_wish_list(self, product_number):
        add_to_wish_list_button = self.find(f'{loc.ADD_TO_WISH_LIST}[{product_number}]')
        add_to_wish_list_button.click()
