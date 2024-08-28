from playwright.sync_api import expect
from pw_test_alex_v.pages.base_page import BasePage


class Account(BasePage):

    def successful_registration_message_displayed_is(self, message_text):
        success_msg = self.page.locator('.messages').inner_text()
        expect(success_msg).to_equal(message_text)
