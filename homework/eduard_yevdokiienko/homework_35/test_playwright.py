from playwright.sync_api import BrowserContext, Page, expect


def test_first(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('//a[contains(text(),"Click")]').click()
    result = page.locator('//p[@id="result-text"]')
    expect(result).to_have_text('Ok')


def test_second(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button_click = page.locator('//a[@id="new-page-button"]')
    with context.expect_page() as new_tab_event:
        button_click.click()
        page2 = new_tab_event.value

    result_tab2 = page2.locator('//p[@id="result-text"]')
    expect(result_tab2).to_have_text('I am a new page in a new tab')
    expect(button_click).to_be_enabled()


def test_third(page: Page):
    page.goto('https://www.demoblaze.com/index.html')
    page.locator('//a[@id="login2"]').click()
    page.locator('//input[@id="loginusername"]').fill('ddfdfwdfwef')
    page.locator('//input[@id="loginpassword"]').fill('ddfdfwdfwef')
    with page.expect_response('https://api.demoblaze.com/login') as response_event:
        page.locator('//button[@onclick="logIn()"]').click()
        response = response_event.value
    assert response.json()['errorMessage'] == 'User does not exist.'
