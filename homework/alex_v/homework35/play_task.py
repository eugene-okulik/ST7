from playwright.sync_api import BrowserContext, Page, expect, Dialog

import pytest
import re


def test_alert(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.on('dialog', lambda alert: alert.accept())
    page.locator(".a-button").click()
    assert page.locator(".result-text").inner_text() == "Ok"


def test_click_enabled(page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with context.expect_page() as new_tab_event:
        click_button = page.locator(".a-button")
        click_button.click()
        page2 = new_tab_event.value

    result_text = page2.locator('#result-text').inner_text()
    expect(click_button).to_be_enabled()
    assert result_text == 'I am a new page in a new tab'


def test_negative_login_data_fill_in(page: Page):
    page.goto('https://www.demoblaze.com/index.html')
    with page.expect_response('**/login') as response_event:
        page.locator('#login2').click()
        page.locator('#loginusername').fill('Cyprus')
        page.locator('#loginpassword').fill('Cyprus')
        page.locator('//button[text()="Log in"]').click()
        response = response_event.value
    assert 'User does not exist.' in response.json()['errorMessage']
