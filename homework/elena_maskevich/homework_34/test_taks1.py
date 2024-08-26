from playwright.sync_api import Page, expect


def test_click_red_button(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    expect(button).to_be_enabled()
    button.click()


def test_fill_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    name_field = page.locator('#firstName')
    name_field.fill('Elena')
    second_name_field = page.locator('#lastName')
    second_name_field.fill('Maskevich')
    email_field = page.locator('#userEmail')
    email_field.fill('maskevich1993@mail.ru')
    gender_checkbox = page.locator('//label[@for="gender-radio-2"]')
    gender_checkbox.click()
    mobile_field = page.locator('#userNumber')
    mobile_field.fill('6786767678')
    date_birth = page.locator('#dateOfBirthInput')
    date_birth.click()
    page.locator('.react-datepicker__month-select').select_option('June')
    page.locator('.react-datepicker__year-select').select_option('1905')
    date_field = page.locator('//div[contains(text(),"24")]')
    date_field.click()
    subject_input = page.locator('#subjectsInput')
    subject_input.fill('s')
    subject_selected = page.locator('#react-select-2-option-1')
    subject_selected.click()
    hobbies_input = page.locator('//label[@for="hobbies-checkbox-2"]')
    hobbies_input.click()
    current_address = page.locator('#currentAddress')
    current_address.click()
    state_and_city = page.locator('#state')
    state_and_city.click()
    state = page.locator('#react-select-3-option-1')
    state.click()
    city = page.locator('#city')
    city.click()
    city = page.locator('#react-select-4-option-0')
    city.click()
    submit_form = page.locator('#submit')
    submit_form.click()
    table_form = page.locator('//tr[1]/td[2]')
    expect(table_form).to_have_text('Elena Maskevich')
