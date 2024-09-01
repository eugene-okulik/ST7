# from selenium.webdriver.common.by import By
from pw_test_alex_v.pages.base_page import BasePage


class CreateAccountPage(BasePage):
    page_url = '/customer/account/create/'

    def fill_in_first_name(self, firstname: str):
        first_name = self.find('#firstname')
        first_name.click()
        first_name.fill(firstname)

    def fill_in_last_name(self, lastname: str):
        last_name = self.find('#lastname')
        last_name.click()
        last_name.fill(lastname)

    def fill_in_email(self, email: str):
        email_field = self.find('input[name="email"]')
        email_field.click()
        email_field.fill(email)

    def fill_in_password(self, password: str):
        password_field = self.find('#password')
        password_field.click()
        password_field.fill(password)

    def fill_in_password_confirmation(self, password_confirm: str):
        password_confirmation_field = self.find('input[name="password_confirmation"]')
        password_confirmation_field.click()
        password_confirmation_field.fill(password_confirm)

    def click_on_create_an_account_button(self):
        create_account_btn = self.find('//button[@title="Create an Account"]')
        create_account_btn.click()

    def invalid_email_notification_message_displayed_is(self, message_text: str) -> bool:
        notification_message = self.find('#email_address-error').inner_text()
        return notification_message == message_text

    def password_notification_message_displayed_is(self) -> str:
        notification_message = self.find('#password-error').inner_text()
        return notification_message

    def confirm_password_notification_message_displayed_is(self, message_text: str) -> bool:
        notification_message = self.find('#password-confirmation-error').inner_text()
        return notification_message == message_text
