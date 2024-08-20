from playwright.sync_api import Page, expect
import re


def test_changing_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    hidden_button = page.get_by_role('button', name='Visible After 5 Seconds')
    expect(hidden_button).to_be_visible(timeout=10000)
    page.get_by_role('button', name='Color Change').click()


def test_fill_the_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.locator('#firstName').fill('firstName')
    page.locator('#lastName').fill('lastName')
    page.locator('#userEmail').fill('user@Email.com')
    page.locator('//label[contains(text(), "Male")]').click()
    page.locator('#userNumber').fill('0123456789')
    page.locator('#dateOfBirthInput').click()
    page.locator('.react-datepicker__month-select').select_option('8')
    page.locator('.react-datepicker__year-select').select_option('1983')
    page.locator('[aria-label="Choose Thursday, September 1st, 1983"]').click()
    page.locator('#subjectsInput').fill('e')
    page.locator('#react-select-2-option-0').click()
    page.locator('//label[contains(text(), "Music")]').click()
    page.locator('#currentAddress').fill('currentAddress')
    page.locator('#state').click()
    page.locator('#react-select-3-option-3').click()
    page.locator('#city').click()
    page.locator('#react-select-4-option-0').click()
    page.locator('#submit').click()
    modal = page.locator('.modal-content')
    expect(modal).to_have_text(re.compile('firstName'))
    expect(modal.get_by_text('firstName lastName')).to_be_visible()
    expect(modal.get_by_text('user@Email.com')).to_be_visible()
