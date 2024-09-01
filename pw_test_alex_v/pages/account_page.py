from playwright.sync_api import expect
from pw_test_alex_v.pages.base_page import BasePage


class Account(BasePage):

    def successful_registration_message_displayed_is(self, message_text: str):
        expect(self.page.locator('.messages')).to_contain_text(message_text)
