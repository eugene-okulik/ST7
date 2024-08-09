import allure
from ui_tests_yevdokiienko.pages.base_page import BasePage
from ui_tests_yevdokiienko.pages.locators import SaleLocators as loc


class MenDealPage(BasePage):
    page_url = '/promotions/men-sale.html'

    @allure.step('Men deal page')
    def check_men_page_opened(self, page_title):
        assert page_title in self.find(loc.MEN_PAGE_TITLE).text
