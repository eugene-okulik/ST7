from playwright.sync_api import Page
from time import sleep


def test_auth_login(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    form_auth = page.get_by_role('link', name='Form Authentication')
    form_auth.click()
    sleep(2)
    username_input = page.get_by_role('textbox', name='username')
    username_input.fill('Kate')
    password_input = page.get_by_role('textbox', name='password')
    password_input.fill('Hushcha')
    submit_button = page.get_by_role('button', name='Login')
    submit_button.click()
    sleep(2)
