from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from ui_test_alex_v.pages.base_page import BasePage


class Account(BasePage):

    def successful_registration_message_displayed_is(self, message_text):
        success_msg = self.find((By.CLASS_NAME, 'messages')).text
        assert success_msg == message_text
