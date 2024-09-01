from pw_test_alex_v.pages.base_page import BasePage

import allure


class CustomerLoginPage(BasePage):
    page_url = '/customer/account/login/'

    def invalid_login_notification_message_displayed_is(self, expected_message: str) -> bool:
        # Locate the alert div using the correct Playwright locator method
        notification_locator = self.page.locator('//div[@role="alert"]')
        notification_locator.first.wait_for(state="visible", timeout=10000)
        notification_message = notification_locator.first.inner_text().strip()
        print(f"Actual notification message: {notification_message}")

        return expected_message.lower() in notification_message.lower()



