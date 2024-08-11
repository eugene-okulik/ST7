import allure
from ui_tests_yevdokiienko.pages.base_page import BasePage
from ui_tests_yevdokiienko.pages.locators import RegisterLocators as loc


class CreateAccountPage(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Fill the form')
    def check_form_is_able(self, page_title):
        assert page_title in self.find(loc.PAGE_TITLE).text

    def fill_first_name(self, first_name):
        self.find(loc.FIRST_NAME).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.find(loc.LAST_NAME).send_keys(last_name)

    def fill_email(self, email):
        self.find(loc.EMAIL).send_keys(email)

    def fill_password(self, password):
        self.find(loc.PASSWORD).send_keys(password)

    def fill_confirm_password(self, confirm_password):
        self.find(loc.CONFIRM_PASSWORD).send_keys(confirm_password)

    def click_create(self):
        self.find(loc.BUTTON_CREATE_ACCOUNT).click()

    def password_confirmation_error(self, error):
        assert error in self.find(loc.PASSWORD_CONFIRM_ERROR).text
