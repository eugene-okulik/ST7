import allure
from ui_tests_yevdokiienko.pages.base_page import BasePage
from ui_tests_yevdokiienko.pages.locators import RegisterLocators as loc
from ui_tests_yevdokiienko.pages.locators import AccountLocators as loc


class AccountPage(BasePage):
    page_url = '/customer/account/'

    @allure.step('Account page')
    def check_registration_success(self, reg_success):
        assert reg_success in self.find(loc.REG_SUCCESS).text

    def check_page_title(self, page_title):
        assert page_title in self.find(loc.PAGE_TITLE).text

    def check_contact_information(self, contact_information):
        assert contact_information in self.find(loc.CONTACT_INFORMATION).text
