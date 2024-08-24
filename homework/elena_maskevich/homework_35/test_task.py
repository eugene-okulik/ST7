from playwright.sync_api import BrowserContext, Page, expect
import pytest


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


def test_alert(page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    result = page.locator('#result-text')
    expect(result).to_have_text('Ok')


def test_tabs(page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with context.expect_page() as new_tab_event:
        page.locator('#new-page-button').click()
        page2 = new_tab_event.value

    result = page2.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    button = page.locator('#new-page-button')
    expect(button).to_be_enabled()


def test_response(page):
    page.goto('https://www.demoblaze.com/index.html')
    page.get_by_role('link', name='Log in').click()
    page.locator('#loginusername').fill('234234534')
    page.locator('#loginpassword').fill('adfoura;fd')
    with page.expect_response('https://api.demoblaze.com/login') as response_event:
        page.locator('//button[@onclick="logIn()"]').click()
        response = response_event.value
    assert response.json()["errorMessage"] == "User does not exist."
