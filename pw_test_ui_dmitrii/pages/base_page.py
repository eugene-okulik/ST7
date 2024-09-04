import allure
from playwright.sync_api import Page, Locator


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None
    locator = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open page')
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

    def find(self, locator: str) -> Locator:
        return self.page.locator(locator).first

    @allure.step('Fill Input by ID')
    def fill_input_by_id(self, locate_id, input_text):
        self.find(f'#{locate_id}').fill(input_text)

    @allure.step('Push the button')
    def push_the_button(self, button_selector):
        print(f'//button[@{button_selector}]')
        self.find(f'//button[@{button_selector}]').click()

    @allure.step('Required field check')
    def check_required_field(self):
        return self.find('//div[contains(text(),"This is a required field.")]').is_visible()

    def check_correct_page_opened(self, text):
        return text in self.find(f'//h1[@id="page-title-heading"]/span[contains(text(), {text})]').inner_text()

    @allure.step('Move attention')
    def move_attention(self, locator):
        target = self.find(locator)
        target.hover()

    # def accept_alert(self):
    #     self.page.on('dialog', lambda dialog: dialog.accept())
    #     self.page.wait_for_event('dialog')
