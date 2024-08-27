import allure
from playwright.sync_api import Page, Locator


class BasePage:
    base_url = 'https://www.demoblaze.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open home page')
    def open(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Unable to open that page by url')

    @allure.step('Scroll the page')
    def scroll_page(self, pixels=None, start=0):
        if pixels:
            self.page.evaluate(f"window.scrollTo({start}, {pixels})")
        else:
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Find element')
    def find(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def accept_alert(self):
        self.page.on('dialog', lambda dialog: dialog.accept())
        self.page.wait_for_event('dialog')
