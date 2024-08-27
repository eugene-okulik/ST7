import allure
from pw_tests_eokulik.pages.base_page import BasePage


class HomePage(BasePage):
    page_url = '/index.html'

    @allure.step('Click product')
    def click_product(self, product_name):
        # product_link = f'//a[text()="{product_name}"]'
        product_link = f'//a[contains(text(), "{product_name}")]'
        self.find(product_link).click()
