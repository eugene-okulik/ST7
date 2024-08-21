from playwright.sync_api import Page, expect


def test_red_color_button(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_button = page.locator('#colorChange')
    expect(color_button).to_have_class('mt-4 text-danger btn btn-primary')
    color_button.click()


def test_form_filling(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.locator('#firstName').type('Katerina')
    page.locator('#lastName').type('Submity')
    page.locator('#userEmail').type('kate.submity@gmail.com')
    page.locator('//label[@for="gender-radio-3"]').click()
    page.locator('#userNumber').type('8482787720')
    dob_field = page.locator('#dateOfBirthInput')
    dob_field.click()
    page.locator('//*[@class="react-datepicker__month-select"]').select_option('February')
    page.locator('//*[@class="react-datepicker__year-select"]').select_option('1991')
    page.locator('//div[@class="react-datepicker__day react-datepicker__day--013"]').click()
    subject_field = page.locator('#subjectsInput')
    subject_field.type('Phy')
    subject_field.press('Enter')
    page.locator('//label[@for="hobbies-checkbox-1"]').click()
    page.locator('#currentAddress').fill('140 Withdraw st, Princeton NJ')
    state_field = page.locator('(//*[@class=" css-1hwfws3"])[1]')
    state_field.click()
    state_select = page.locator('#react-select-3-option-2')
    state_select.click()
    city_field = page.locator('(//*[@class=" css-1hwfws3"])[2]')
    city_field.click()
    city_select = page.locator('#react-select-4-option-1')
    city_select.click()
    page.locator('#submit').click()
    user_email = page.locator('//td[text()="Student Email"]/following-sibling::td')
    expect(user_email).to_have_text('kate.submity@gmail.com')
