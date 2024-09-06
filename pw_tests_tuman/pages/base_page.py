import allure
from playwright.sync_api import Page, Locator, expect


class Basepage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open home pages')
    def open(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}', wait_until='domcontentloaded')
        else:
            raise NotImplementedError('Unable to open that pages by url')

    def find(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def is_equal(self, locator: str, text: str):
        expect(self.page.locator(locator)).to_have_text(text)
        return True

    def click_el(self, locator: str):
        self.find(locator).click()

    def current_url_is(self, url: str):
        expect(self.page).to_have_url(url)
        return True

    def wait_for_element_visible(self, selector: str, timeout: int = 10000) -> Locator:
        locator = self.page.locator(selector).first
        expect(locator).to_be_visible(timeout=timeout)
        return locator
