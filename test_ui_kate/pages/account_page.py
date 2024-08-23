import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import Locators as loc


class AccountPage(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Checking the strength of the password')
    def password_strength(self, text):
        assert text in self.find(loc.PASSWORD_STRENGTH_WEAK).text

    @allure.step('Checking entering an incorrect email address')
    def invalid_email_error(self, text):
        assert self.find(loc.INVALID_EMAIL_ERROR).text == text
