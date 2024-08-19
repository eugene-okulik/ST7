from playwright.sync_api import BrowserContext, Page, Dialog, expect
import re
import pytest
from time import sleep


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_viewport_size({'width': 1520, 'height': 980})
    return page


def test_alert(page: Page):

    def handle_alert(alert: Dialog):
        alert.accept()

    sleep(3)
    page.on('dialog', handle_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm',
              wait_until='domcontentloaded')
    page.get_by_role('link', name='Click').click()
    sleep(3)

    result_text = page.locator('.result-text')
    expect(result_text).to_have_text('Ok')


def test_aller_tabs(page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with context.expect_page() as new_page_event:
        btn_click = page.get_by_role('link', name='Click')
        btn_click.click()

    page2 = new_page_event.value
    result = page2.locator('.result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(btn_click).to_be_enabled()


def test_request(page):
    page.goto('https://www.demoblaze.com/index.html', wait_until='domcontentloaded')
    with page.expect_response('**/login') as response_evn:
        page.get_by_role('link', name='Log in').click()
        sleep(1)
        page.locator('#loginusername').type('maylo')
        page.locator('#loginpassword').type('234234')
        sleep(1)
        page.get_by_role('button', name='Log in').click()
        response = response_evn.value
    assert 'User does not exist.' == response.json()['errorMessage']
