from playwright.sync_api import Page, expect


def test_hero_site(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    form_auth = page.get_by_role('link', name='Form Authentication')
    form_auth.click()
    username = page.get_by_role('textbox', name='username')
    username.fill('Jonhy')
    password = page.get_by_role('textbox', name='password')
    password.fill('cyberpunk2077')
    login = page.get_by_role('button', name='Login')
    login.click()
