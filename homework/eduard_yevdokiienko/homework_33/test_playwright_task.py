from playwright.sync_api import Page, expect


def test_heroku(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('login')
    page.get_by_role('textbox', name='password').fill('password')
    page.get_by_role('button', name=' Login').click()
    flash_element = page.locator('#flash')
    expect(flash_element).to_contain_text('Your username is invalid!')
