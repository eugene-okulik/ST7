from pw_test_alex_v.pages.base_page import BasePage

import allure


class CustomerLoginPage(BasePage):
    page_url = '/customer/account/login/'

    def invalid_login_notification_message_displayed_is(self, expected_message: str) -> bool:
        notification_locator = self.find('//div[@role="alert"]')
        notification_locator.wait_for(state="visible", timeout=10000)
        notification_message = notification_locator.inner_text().strip()
        return expected_message.lower() in notification_message.lower()
