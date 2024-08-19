import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import AccountLocators as loc


class AccountPage(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Finding a field for filling up')
    def find_field(self, locator):
        self.find(locator).click()

    @allure.step('Sending values to fields')
    def send_keys(self, key_value):
        self.actions_send_keys(key_value)

    @allure.step('Checking the strength of the password')
    def weak_password(self):
        assert 'Weak' in self.find(loc.PASSWORD_WEAK).text

    @allure.step('Checking entering an incorrect email address')
    def invalid_email(self):
        assert self.find(loc.INVALID_EMAIL).text == 'Please enter a valid email address (Ex: johndoe@domain.com).'
