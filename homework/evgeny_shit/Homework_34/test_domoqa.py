from playwright.sync_api import Page, expect


def test_color_change_click(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    expect(button).to_have_class("mt-4 text-danger btn btn-primary")
    button.click()


def test_fill_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    first_name = page.locator('#firstName')
    first_name.fill('Evgeny')

    last_name = page.locator('#lastName')
    last_name.fill('Shit')

    email = page.locator('#userEmail')
    email.fill('X0XUa@example.com')

    male = page.locator('//label[@for="gender-radio-1"]')
    male.click()

    phone = page.locator('#userNumber')
    phone.fill('9999998608')

    date_of_birth = page.locator('#dateOfBirthInput')
    date_of_birth.click()
    month = page.locator('//*[@class="react-datepicker__month-select"]')
    month.select_option('January')
    year = page.locator('//*[@class="react-datepicker__year-select"]')
    year.select_option('1990')
    day = page.locator('//div[@class="react-datepicker__day react-datepicker__day--024"]')
    day.click()

    subjects = page.locator('#subjectsInput')
    subjects.type('Maths')
    auto_complete = page.locator('#react-select-2-option-0')
    auto_complete.click()

    hobby = page.locator('//label[@for="hobbies-checkbox-3"]')
    hobby.click()

    address = page.locator('#currentAddress')
    address.fill('some adress')

    state = page.locator('(//*[@class=" css-1hwfws3"])[1]')
    state.click()
    option_state = page.locator('#react-select-3-option-1')
    option_state.click()

    city = page.locator('(//*[@class=" css-1hwfws3"])[2]')
    city.click()
    option_city = page.locator('#react-select-4-option-2')
    option_city.click()

    submit = page.locator('#submit')
    submit.click()

    stud_name = page.locator('//td[text()="Student Name"]/following-sibling::td')
    expect(stud_name).to_have_text('Evgeny Shit', timeout=1000)
