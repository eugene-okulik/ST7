import time

from playwright.sync_api import Page, expect
import re


def test_google(page: Page):
    page.goto('https://www.google.com/')
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    search_field.press('Enter')
    # assert 'cat' in page.title()
    # assert page.title().startswith('cat')
    expect(page).to_have_title(re.compile('cat'))  # assert 'cat' in page.title()
    expect(page).to_have_title(re.compile('^cat'))  # assert page.title().startswith('cat')


def test_by_role(page: Page):
    page.goto('https://www.demoblaze.com/index.html')
    laptops = page.get_by_role('link', name='Laptops')
    laptops.click()
    time.sleep(1)
    phones = page.get_by_role('link', name='Phones')
    phones.click()
    time.sleep(3)
