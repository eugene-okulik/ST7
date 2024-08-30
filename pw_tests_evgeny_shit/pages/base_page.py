from playwright.sync_api import Page, Locator, expect


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

    def find_elements(self, selector: str) -> list[Locator]:
        return self.page.locator(selector).all()

    def click_element(self, selector: str) -> None:
        self.page.click(selector)

    def current_url_is_(self, url: str) -> bool:
        expect(self.page).to_have_url(url)
        return True

    def is_equal(self, selector: str, text: str) -> bool:
        expect(self.page.locator(selector)).to_have_text(text)
        return True
