import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import Locators as loc


class AccountPage(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Typing a weak password')
    def type_password(self, text):
        self.find_and_click_element(loc.PASSWORD_FIELD)
        self.send_keys_to_element(text)

    @allure.step('Checking the strength of the password')
    def check_password_strength(self, text):
        assert text in self.find_element(loc.PASSWORD_STRENGTH_WEAK).text

    @allure.step('Find and click create button')
    def click_create_account_button(self):
        self.find_and_click_element(loc.CREATE_BUTTON)

    @allure.step('Checking entering an incorrect email address')
    def check_invalid_email_error(self, text):
        assert self.find_element(loc.INVALID_EMAIL_ERROR).text == text

    @allure.step('Enter the first name')
    def enter_first_name(self, f_name):
        self.find_and_click_element(loc.FIRST_NAME_FIELD)
        self.send_keys_to_element(f_name)

    @allure.step('Enter the last name')
    def enter_last_name(self, l_name):
        self.find_and_click_element(loc.LAST_NAME_FIELD)
        self.send_keys_to_element(l_name)

    @allure.step('Enter the email')
    def enter_email_address(self, email):
        self.find_and_click_element(loc.EMAIL_FIELD)
        self.send_keys_to_element(email)

    @allure.step('Confirm the password')
    def confirm_password(self, text):
        self.find_and_click_element(loc.CONFIRM_PASSWORD_FIELD)
        self.send_keys_to_element(text)
