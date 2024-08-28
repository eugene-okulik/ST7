from playwright.sync_api import expect
from pw_tests_tuman.pages.base_page import Basepage
from pw_tests_tuman.pages.locators import CreateAccount as loc

import pytest


class CreateAccountPage(Basepage):
    page_url = 'customer/account/create/'

    def input_met(self, loc, send_text):
        self.find(loc).type(send_text)

    def check_message_error(self, text):
        return self.equal(loc.error_message, text)

    def check_text_is(self, text):
        found_el = self.find(loc.error_message)
        # assert found_el.text == text
        expect(found_el).to_have_text(text)

    def spase_name(self):
        text_spase_error = self.find_element(loc.spase_input)
        text_spase_error.type('')
        expect(text_spase_error).to_have_text('This is a required field.')
        # assert text_spase_error.text == 'This is a required field.'
