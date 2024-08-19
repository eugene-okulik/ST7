from playwright.sync_api import Page, expect, BrowserContext


def test_alert_accept(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.on('dialog', lambda alert: alert.accept())
    page.locator('//a[@onclick]').first.click()
    assert page.locator('#result-text').inner_text() == 'Ok'


def test_tabs_status(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with context.expect_page() as new_tab_event:
        button = page.locator('#new-page-button')
        button.click()
        page2 = new_tab_event.value

    result = page2.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(button).to_be_enabled()


def test_error_message(page: Page):
    page.goto('https://www.demoblaze.com/index.html')
    with page.expect_response('**/login') as response_event:
        page.locator('#login2').click()
        page.locator('#loginusername').fill('QWERasd')
        page.locator('#loginpassword').fill('QWERasd')
        page.locator('//button[text()="Log in"]').click()
        response = response_event.value

    assert response.json().get('errorMessage') == 'User does not exist.', \
        f"Expected error message 'User does not exist.', but got {response.json().get('errorMessage')}"
