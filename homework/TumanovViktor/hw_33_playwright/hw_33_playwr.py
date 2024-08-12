from playwright.sync_api import Page, expect
import time


def test_form(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    authentication = page.get_by_role('link', name='Form Authentication')
    authentication.click()
    time.sleep(1)
    user_name = page.get_by_role('textbox', name='username')
    user_name.fill('vitek')
    user_name = page.get_by_role('textbox', name='password')
    user_name.fill('123456zZ!')
    login_button = page.get_by_role('button', name='Login')
    login_button.click()
