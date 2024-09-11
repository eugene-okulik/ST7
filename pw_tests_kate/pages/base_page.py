import allure
from playwright.sync_api import Page, Locator, expect
from pw_tests_kate.pages.locators import Locators as loc


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Opening the page')
    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Unable to open that page by url')

    @allure.step('Finding an element')
    def find_element_by_locator(self, locator: str) -> Locator:
        return self.page.locator(locator).first

    @allure.step('Finding an element by role')
    def find_element_by_role(self, locator):
        return self.page.get_by_role(locator)

    @allure.step('Find an element and click')
    def find_and_click_element(self, locator):
        self.find_element_by_locator(locator).click()

    @allure.step('Sending keys to an element')
    def send_keys_to_element(self, locator, key_value):
        self.page.locator(locator).type(key_value, timeout=50000)

    @allure.step('Moving to an element')
    def move_to_element(self, locator):
        self.page.locator(locator).hover()

    @allure.step('Checking the page title')
    def check_page_title(self, title):
        expect(self.page.locator(loc.HEADER)).to_contain_text(title)
