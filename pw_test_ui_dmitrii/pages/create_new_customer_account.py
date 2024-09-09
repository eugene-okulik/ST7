import allure
from pw_test_ui_dmitrii.pages.base_page import BasePage
import string
import secrets


class NewCustomerAccount(BasePage):
    page_url = 'customer/account/create/'

    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

    @allure.step('Password Generation')
    def fill_password_input(self, locate_id='password', length=12):
        self.password = self.generate_password(length)
        self.fill_input_by_id(locate_id, self.password)
        return self.password

    def fill_password_confirmation(self, confirmation_password=None, locate_id='password-confirmation'):
        if not confirmation_password:
            confirmation_password = self.password
        self.fill_input_by_id(locate_id, confirmation_password)

    @allure.step('Check incorrect password to confirm')
    def check_incorrect_password_to_confirm(self):
        return self.find('#password-confirmation-error').is_visible()

    @allure.step('Fill Name Input')
    def fill_name_input(self, name):
        self.fill_input_by_id('firstname', name)

    @allure.step('Fill Surname Input')
    def fill_surname_input(self, name):
        self.fill_input_by_id('lastname', name)

    @allure.step('Fill email Input')
    def fill_email_input(self, name):
        self.fill_input_by_id('email_address', name)

    @allure.step('Push "Create account" button')
    def push_create_account_button(self):
        self.push_the_button('title="Create an Account"')