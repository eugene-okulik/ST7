from playwright.sync_api import Page, expect


def test_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')

    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('Evgeny')
    page.get_by_role('textbox', name='password').fill('passwordQ1')
    page.get_by_role('button', name='Login').click()

    error_mes = page.locator('#flash.flash.error')
    expect(error_mes).to_be_visible()
    expect(error_mes).to_contain_text('Your username is invalid!')
