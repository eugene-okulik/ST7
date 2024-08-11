from playwright.sync_api import Page


def test_herokuapp(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    auth = page.get_by_role('link', name='Form Authentication')
    auth.click()
    login_input = page.get_by_role('textbox', name='username')
    login_input.fill('Elena')
    password_input = page.get_by_role('textbox', name='password')
    password_input.fill('123')
    button = page.get_by_role('button')
    button.click()
