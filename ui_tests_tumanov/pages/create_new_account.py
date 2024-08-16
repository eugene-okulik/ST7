from ui_tests_tumanov.pages.base_page import Basepage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ui_tests_tumanov.pages.locators import CreateAccount as loc

from ui_tests_tumanov.pages.locators import CreateAccount
import pytest


class CreateAccountPage(Basepage):
    page_url = 'customer/account/create/'

    def input_met(self, loc, send_text):
        self.driver.find_element(*loc).send_keys(send_text)

    # def check_message_error(self, text):
    #     wait = WebDriverWait(self.driver, 5)
    #     text_error_message = wait.until(ec.visibility_of_element_located(loc.error_message))
    #     assert text_error_message.text == text

    def check_text_is(self, text):
        found_el = self.find(loc.error_message)
        assert found_el.text == text

    def spase_name(self):
        wait = WebDriverWait(self.driver, 5)
        text_spase_error = wait.until(ec.visibility_of_element_located(loc.spase_input))
        assert text_spase_error.text == 'This is a required field.'
