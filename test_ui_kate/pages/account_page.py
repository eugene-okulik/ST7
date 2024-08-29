import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import Locators as loc


class AccountPage(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Find and click password field')
    def click_password_input_field(self):
        self.find_and_click_element(loc.PASSWORD_FIELD)

    @allure.step('Typing a weak password')
    def type_weak_password(self):
        self.send_keys_to_element('Barsuki')

    @allure.step('Checking the strength of the password')
    def check_password_strength(self, text):
        assert text in self.find_element(loc.PASSWORD_STRENGTH_WEAK).text

    @allure.step('Find and click email field')
    def click_email_input_field(self):
        self.find_and_click_element(loc.EMAIL_FIELD)

    @allure.step('Typing an incorrect email address')
    def type_incorrect_email(self):
        self.send_keys_to_element('skdfjg.com')

    @allure.step('Find and click create button')
    def click_create_account_button(self):
        self.find_and_click_element(loc.CREATE_BUTTON)

    @allure.step('Checking entering an incorrect email address')
    def check_invalid_email_error(self, text):
        assert self.find_element(loc.INVALID_EMAIL_ERROR).text == text

    @allure.step('Find and click first name field')
    def click_first_name_input_field(self):
        self.find_and_click_element(loc.FIRST_NAME_FIELD)

    @allure.step('Enter the first name')
    def type_first_name(self):
        self.send_keys_to_element('Kate')

    @allure.step('Find and click last name field')
    def click_last_name_input_field(self):
        self.find_and_click_element(loc.LAST_NAME_FIELD)

    @allure.step('Enter the last name')
    def type_last_name(self):
        self.send_keys_to_element('Test')

    @allure.step('Find and click email field')
    def click_email_input_field(self):
        self.find_and_click_element(loc.EMAIL_FIELD)

    @allure.step('Enter the email')
    def type_email_address(self):
        self.send_keys_to_element('katetestXYZ@yahoo.com')

    @allure.step('Find and click password field')
    def click_password_input_field(self):
        self.find_and_click_element(loc.PASSWORD_FIELD)

    @allure.step('Enter a password')
    def type_password(self):
        self.send_keys_to_element('Barsuki07')

    @allure.step('Find and click confirmation password field')
    def click_confirmation_password_input_field(self):
        self.find_and_click_element(loc.CONFIRM_PASSWORD_FIELD)

    @allure.step('Confirm the password')
    def type_password_again(self):
        self.send_keys_to_element('Barsuki07')    
