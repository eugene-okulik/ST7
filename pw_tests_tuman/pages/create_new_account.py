from playwright.sync_api import expect, Locator
from pw_tests_tuman.pages.base_page import Basepage
from pw_tests_tuman.pages.locators import CreateAccount as loc
from time import sleep


class CreateAccountPage(Basepage):
    page_url = 'customer/account/create/'

    def filling_out_the_form(self, first_name, last_name, email, password, password_confirmation):
        self.data_form(loc.first_name_loc, first_name)
        self.data_form(loc.last_name_loc, last_name)
        self.data_form(loc.email_loc, email)
        self.data_form(loc.password_loc, password)
        self.data_form(loc.password_confirmation_loc, password_confirmation)

    def click_button_create(self):
        self.click_el(loc.click_button_account)

    def data_form(self, locator: str, text: str):
        self.page.fill(locator, text)

    def check_message_error(self, text):
        return self.is_equal(loc.error_message, text)

    def check_text_is(self, text):
        found_el = self.find(loc.error_message)
        # assert found_el.text == text
        expect(found_el).to_have_text(text)
        # заменил на timeout=10000 не помогло

    def check_empty_input_message(self, text: str):
        sleep(3)
        # self.find(loc.first_name_loc).click()
        # self.find(loc.first_name_loc).page.keyboard.press('Enter')
        self.click_el(loc.click_button_account)
        sleep(3)
        support_text = self.find(loc.support_text)
        expect(support_text).to_have_text()
        text_spase_error = self.find(loc.spase_input)
        expect(text_spase_error).to_have_text(text, timeout=10000)
# Так и не понял как это победить