from playwright.sync_api import Page, expect, BrowserContext


def test_1_alert(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    result_text = page.locator('#result-text')
    expect(result_text).to_be_visible()
    expect(result_text).to_have_text('Ok')


def test_2_tab(page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button = page.get_by_role('link', name='Click')
    with context.expect_page() as new_tab_event:
        button.click()
        page2 = new_tab_event.value

    result = page2.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(button).to_be_enabled()


def test_3_unbelievable_user(page):
    kind_of_tree = 'someshit'
    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()
    page.locator('#loginusername').fill(kind_of_tree)
    page.locator('#loginpassword').fill(kind_of_tree)
    with page.expect_response('https://api.demoblaze.com/login') as response_event:
        page.get_by_role('button', name='Log in').click()
        response = response_event.value

    assert response.json()['errorMessage'] in ('User does not exist.', 'Wrong password.')
