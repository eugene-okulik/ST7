import allure
from playwright.sync_api import expect
from pw_tests_yevdokiienko.pages.base_page import BasePage
from pw_tests_yevdokiienko.pages.locators import RegisterLocators as loc


class CreateAccountPage(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Fill the form')
    def check_form_is_able(self, page_title):
        expect(self.find(loc.PAGE_TITLE)).to_contain_text(page_title)

    def fill_first_name(self, first_name):
        self.find(loc.FIRST_NAME).fill(first_name)

    def fill_last_name(self, last_name):
        self.find(loc.LAST_NAME).fill(last_name)

    def fill_email(self, email):
        self.find(loc.EMAIL).fill(email)

    def fill_password(self, password):
        self.find(loc.PASSWORD).fill(password)

    def fill_confirm_password(self, confirm_password):
        self.find(loc.CONFIRM_PASSWORD).fill(confirm_password)

    def click_create(self):
        self.find(loc.BUTTON_CREATE_ACCOUNT).click()

    def password_confirmation_error(self, error):
        expect(self.find(loc.PASSWORD_CONFIRM_ERROR)).to_contain_text(error)
