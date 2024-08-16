from playwright.sync_api import BrowserContext, Page, expect, Dialog

import pytest

from time import sleep


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    # page.set_viewport_size({'width': 920, 'height': 500})
    return page


def test_tabs(page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/link')
    with context.expect_page() as new_tab_event:
        page.locator('#new-page-link').click()
        page2 = new_tab_event.value

    result = page2.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    page.locator('#new-page-link').click()
    sleep(3)


def test_alert(page):

    # def handle_alert(alert: Dialog):
    #     print(alert.type)
    #     print(alert.message)
    #     alert.dismiss()

    def handle_alert(alert: Dialog):
        alert.accept('salkdjflshfiouqwoiefhsfd')

    page.on('dialog', handle_alert)
    # page.on('dialog', lambda alert: alert.dismiss())
    # page.on('dialog', lambda alert: alert.accept('salkdjflshfiouqwoiefhsfd'))
    page.goto('https://www.qa-practice.com/elements/alert/prompt')
    page.get_by_role('link', name='Click').click()
    sleep(5)


def test_vivino(page):
    page.goto('https://www.vivino.com/', wait_until='domcontentloaded')
    page.locator('.css-14ngluw-componentChildren').click()
    sleep(3)
