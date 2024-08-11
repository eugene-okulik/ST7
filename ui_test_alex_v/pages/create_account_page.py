from selenium.webdriver.common.by import By
from ui_test_alex_v.pages.base_page import BasePage


class CreateAccountPage(BasePage):
    page_url = '/customer/account/create/'

    def fill_in_first_name(self, firstname):
        first_name = self.find((By.ID, 'firstname'))
        first_name.click()
        first_name.send_keys(firstname)

    def fill_in_last_name(self, lastname):
        first_name = self.find((By.ID, 'lastname'))
        first_name.click()
        first_name.send_keys(lastname)

    def fill_in_email(self, email):
        first_name = self.find((By.NAME, 'email'))
        first_name.click()
        first_name.send_keys(email)

    def fill_in_password(self, password):
        first_name = self.find((By.ID, 'password'))
        first_name.click()
        first_name.send_keys(password)

    def fill_in_password_confirmation(self, password_confirm):
        first_name = self.find((By.NAME, 'password_confirmation'))
        first_name.click()
        first_name.send_keys(password_confirm)

    def click_on_create_an_account_button(self):
        create_account_btn = self.find((By.XPATH, '//button[@title="Create an Account"]'))
        create_account_btn.click()

    def invalid_email_notification_message_displayed_is(self, message_text):
        notification_message = self.find((By.ID, 'email_address-error')).text
        assert notification_message == message_text

    def password_notification_message_displayed_is(self):
        notification_message = self.find((By.ID, 'password-error'))
        return notification_message.text

    def confirm_password_notification_message_displayed_is(self, message_text):
        notification_message = self.find((By.ID, 'password-confirmation-error')).text
        print(notification_message)
        assert notification_message == message_text
