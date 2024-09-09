import allure
from pw_tests_kate.pages.base_page import BasePage, expect
from pw_tests_kate.pages.locators import Locators as loc


class AccountPage(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Typing a weak password')
    def type_password(self, text):
        self.send_keys_to_element(loc.PASSWORD_FIELD, key_value=text)

    @allure.step('Checking the strength of the password')
    def check_password_strength(self, text):
        expect(self.find_element_by_locator(loc.PASSWORD_STRENGTH_WEAK)).to_have_text(text)

    @allure.step('Find and click create button')
    def click_create_account_button(self):
        self.find_and_click_element(loc.CREATE_BUTTON)

    @allure.step('Checking entering an incorrect email address')
    def check_invalid_email_error(self, text):
        expect(self.find_element(loc.INVALID_EMAIL_ERROR)).to_have_text(text)

    @allure.step('Enter the first name')
    def enter_first_name(self, f_name):
        self.send_keys_to_element(loc.FIRST_NAME_FIELD, key_value=f_name)

    @allure.step('Enter the last name')
    def enter_last_name(self, l_name):
        self.send_keys_to_element(loc.LAST_NAME_FIELD, key_value=l_name)

    @allure.step('Enter the email')
    def enter_email_address(self, email):
        self.send_keys_to_element(loc.EMAIL_FIELD, key_value=email)

    @allure.step('Confirm the password')
    def confirm_password(self, text):
        self.send_keys_to_element(loc.CONFIRM_PASSWORD_FIELD, key_value=text)
