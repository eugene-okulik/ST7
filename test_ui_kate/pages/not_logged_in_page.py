import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import AccountLocators as loc


class NotLoggedIn(BasePage):
    page_url = (
        '/customer/account/login/referer/'
        'aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS93aXNobGlzdC9pbmRleC9hZGQv/'
    )

    @allure.step('Checking not logged in page')
    def erro_without_login(self, locator):
        assert self.find(locator).is_displayed
