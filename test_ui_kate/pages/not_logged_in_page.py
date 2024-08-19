import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import AccountLocators as loc


class NotLoggedIn(BasePage):
    page_url = '/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS93aXNobGlzdC9pbmRleC9hZGQv/'

    @allure.step('Checking not logged in page')
    def find_error_alert(self):
        assert self.find(loc.ERROR_MESSAGE).is_displayed
