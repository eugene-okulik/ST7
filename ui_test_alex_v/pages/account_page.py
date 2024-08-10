from selenium.webdriver.common.by import By

from ui_test_alex_v.pages.base_page import BasePage


class AccountPage(BasePage):
    page_url = '/customer/account/create/'

    def fill_in_first_name(self):
        first_name = self.find(By.ID,'firstname')