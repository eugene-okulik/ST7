import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import AccountLocators as loc


class CustomerAccountPage(BasePage):
    page_url = '/customer/account/'

    @allure.step('Checking a successful registration')
    def success_confirmation(self):
        assert self.find(loc.SUCCESS_CONFIRMATION).text == 'Thank you for registering with Main Website Store.'
