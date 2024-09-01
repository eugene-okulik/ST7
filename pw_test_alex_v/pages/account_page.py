from playwright.sync_api import expect
from pw_test_alex_v.pages.base_page import BasePage


class Account(BasePage):

    def successful_registration_message_displayed_is(self, message_text: str) -> bool:
        message_locator = self.page.locator(
            "//div[contains(text(),'Thank you for registering with Main Website Store.')]")

        try:
            message_locator.wait_for(state="visible", timeout=10000)
            return message_locator.text_content() and message_text.lower() in message_locator.text_content().lower()
        except TimeoutError:
            return False

