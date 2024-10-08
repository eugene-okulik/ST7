from pw_test_ui_dmitrii.pages.base_page import BasePage
import allure


class ProductPage(BasePage):

    def check_opened_correct_product_page(self, string):
        locator = '//span[@itemprop="name"]'
        assert string in self.find(locator).inner_text()

    @allure.step('Open Eco Product Page')
    def open_eco_product(self, page_url):
        self.page_url = page_url
        self.open()
