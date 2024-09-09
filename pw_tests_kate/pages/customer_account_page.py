import allure
from playwright.sync_api import expect
from pw_tests_kate.pages.base_page import BasePage
from pw_tests_kate.pages.locators import Locators as loc


class CustomerAccountPage(BasePage):
    page_url = '/customer/account/'

    @allure.step('Checking a successful registration')
    def confirm_successful_registration(self, text):
        expect(self.find_element(loc.SUCCESS_CONFIRMATION)).to_have_text(text)
