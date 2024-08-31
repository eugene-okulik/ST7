import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import Locators as loc


class NotLoggedIn(BasePage):
    page_url = (
        '/customer/account/login/referer/'
        'aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS93aXNobGlzdC9pbmRleC9hZGQv/'
    )

    @allure.step('Checking cannot add an item without logging in')
    def check_item_not_added_without_logging_in(self):
        assert self.find_element(loc.ERROR_MESSAGE).is_displayed
