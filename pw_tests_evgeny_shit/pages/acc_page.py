from playwright.sync_api import Locator, expect

from pw_tests_evgeny_shit.pages.base_page import BasePage
from pw_tests_evgeny_shit.locators import CreateAccountLocators as loc


class AccountPage(BasePage):
    page_url = '/customer/account/create/'

    def fill_in_reg_form(self, first_name, last_name, email, password):
        self.send_keys(loc.first_name_input, first_name)
        self.send_keys(loc.last_name_input, last_name)
        self.send_keys(loc.email_input, email)
        self.send_keys(loc.password_input, password)
        self.send_keys(loc.password_confirm_input, password)
        self.click_element(loc.creat_acc_button)

    def send_keys(self, selector: str, text: str) -> None:
        self.page.fill(selector, text)

    def click_submit_button(self):
        self.click_element(loc.creat_acc_button)

    def wait_for_error_message(self):
        self.wait_for_element_visible(loc.error_message)

    def error_message_text_is_(self, text: str) -> bool:
        return self.is_equal(loc.error_message, text)

    def number_of_required_fields_is_(self, count: int) -> bool:
        elements = self.find_elements(loc.required_fields)
        return len(elements) == count

    def wait_for_element_visible(self, selector: str, timeout: int = 10000) -> Locator:
        locator = self.page.locator(selector).first
        expect(locator).to_be_visible(timeout=timeout)
        return locator
