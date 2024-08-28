import allure
from playwright.async_api import Locator
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from playwright.sync_api import Page


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Unable to open that page by url')

    @allure.step('Find element')
    def find(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def title_page_is(self, text):
        return self.page.title == text

    def element_visible_is(self, locator):
        return self.find(locator).is_disabled()
