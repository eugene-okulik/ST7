from playwright.sync_api import expect
from pw_test_alex_v.pages.base_page import BasePage


class Account(BasePage):

    def successful_registration_message_displayed_is(self, message_text: str) -> bool:
        success_msg = self.page.locator('.messages').first.inner_text()
        return message_text.lower() in success_msg.lower()
