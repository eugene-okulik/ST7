import allure
from playwright.sync_api import expect
from pw_tests_yevdokiienko.pages.base_page import BasePage
from pw_tests_yevdokiienko.pages.locators import AccountLocators as loc


class AccountPage(BasePage):
    page_url = '/customer/account/'

    @allure.step('Account page')
    def check_registration_success(self, reg_success):
        expect(self.find(loc.REG_SUCCESS)).to_contain_text(reg_success)

    def check_page_title(self, page_title):
        expect(self.find(loc.PAGE_TITLE)).to_contain_text(page_title)

    def check_contact_information(self, contact_information):
        expect(self.find(loc.CONTACT_INFORMATION)).to_contain_text(contact_information)
