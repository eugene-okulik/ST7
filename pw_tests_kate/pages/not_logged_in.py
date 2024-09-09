import allure
from pw_tests_kate.pages.base_page import BasePage
from pw_tests_kate.pages.locators import Locators as loc
from playwright.sync_api import expect


class NotLoggedIn(BasePage):
    page_url = (
        '/customer/account/login/referer/'
        'aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS93aXNobGlzdC9pbmRleC9hZGQv/'
    )

    @allure.step('Checking cannot add an item without logging in')
    def check_item_not_added_without_logging_in(self):
        self.page.wait_for_selector(loc.ERROR_MESSAGE, timeout=30000)
        expect(self.find_element_by_locator(loc.ERROR_MESSAGE)).to_be_visible()
