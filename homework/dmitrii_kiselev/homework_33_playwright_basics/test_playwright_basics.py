from playwright.sync_api import Page, expect
import re


def test_smth(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('tomsmith')
    page.get_by_role('textbox', name='password').fill('SuperSecretPassword!')
    page.get_by_role('button', name=(re.compile('Login'))).click()
    expect(page).to_have_title(re.compile('The Internet'))
