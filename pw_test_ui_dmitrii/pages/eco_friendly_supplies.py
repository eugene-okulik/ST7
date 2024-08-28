import allure
from pw_test_ui_dmitrii.pages.base_page import BasePage


class EcoProducts(BasePage):
    page_url = 'collections/eco-friendly.html'

    @allure.step('Choose Eco product')
    def choose_eco_product(self, locator_text):
        product_page = self.find(f'//a[contains(text(), "{locator_text}")]')
        url_link = product_page.get_attribute('href')
        self.eco_product_page_url = url_link[url_link.find('.com/') + 5:]
        product_page.click()

    @allure.step('Add to favorite')
    def click_to_favorite(self, locator):
        self.find(locator).click()

    @allure.step('Sorting by parameter')
    def sorting_by_(self, locator_1, locator_2):
        self.find(locator_1).select_option(locator_2)

    @allure.step('Check cheapest product is first')
    def check_order_by_price(self, locator):
        # self.page.wait_for_url('**?product_list_order=price**')  # Не работает такой хардкод, поэтому костыль ниже
        for i in range(5):
            if '$18' in self.find(locator).inner_text():
                return True
            else:
                self.page.wait_for_timeout(500)
