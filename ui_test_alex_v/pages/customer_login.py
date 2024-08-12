from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from ui_test_alex_v.pages.base_page import BasePage


class CustomerLoginPage(BasePage):
    def invalid_login_notification_message_displayed_is(self, expected_message):
        notification_element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//div[@role='alert']"))
        )
        notification_message = notification_element.text.strip()
        return expected_message.lower() in notification_message.lower()
