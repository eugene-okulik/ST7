from playwright.sync_api import BrowserContext, Page, expect
import re


def test_alert_conf(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    conf_modal = page.locator('#result-text')
    expect(conf_modal).to_have_text('Ok')


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with context.expect_page() as new_tab_event:
        click_button = page.locator('#new-page-button')
        click_button.click()
        second_page = new_tab_event.value

    end_result = second_page.locator('#result-text')
    expect(end_result).to_have_text('I am a new page in a new tab')
    expect(click_button).to_be_enabled


def test_login_incorrect(page: Page):
    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()
    with page.expect_response(re.compile('/login')) as response_event:
        page.locator('#loginusername').fill('skhdgfmn')
        page.locator('#loginpassword').fill('32746sjdghf')
        page.locator('//button[@class="btn btn-primary" and text()="Log in"]').click()
        response = response_event.value
    assert response.json()['errorMessage'] == 'User does not exist.'
