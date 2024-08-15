from playwright.sync_api import Page, expect


def test_task_one(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button_color = page.locator('#colorChange')
    expect(button_color).to_have_class('mt-4 text-danger btn btn-primary')
    button_color.click()


def test_task_two(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')

    first_name = page.locator('#firstName')
    first_name.type('Vitek')

    last_name = page.locator('#lastName')
    last_name.type('Tuman')

    email = page.locator('#userEmail')
    email.type('test@bk.com')

    page.locator('//label[@for="gender-radio-3"]').click()   # radio other

    mobile_number = page.locator('//*[@id="userNumber"]')
    mobile_number.type('89991112233')

    page.locator('#dateOfBirthInput').click()    # dropdown_data_birtch

    birth_data = page.locator('#react-datepicker__year-select')
    birth_data.click()

    birth_year = page.locator('//*[@value="1993"]')
    birth_year.click()

    month = page.locator('react-datepicker__month-select')
    month.click()

    month = page.locator('//*[@value="7"]')
    month.click()

    day = page.locator('//*[@class="react-datepicker__day react-datepicker__day--023"]')
    day.click()

    box = page.locator('//label[@for="hobbies-checkbox-1"]')
    box.click()

    current_text_address = page.locator('//*[@id="currentAddress"]')
    current_text_address.type('Naro-Fominsk,  1')

    select_state_drop = page.locator('//*[@id="react-select-3-input"]')
    select_state_drop.type('NRC')
    select_state_drop.click()
    city = page.locator('//*[@id="react-select-4-input"]')
    city.type('Delhi')
    city.click()

    page.locator('submit').click()

# Check name
    first_name = page.locator('#firstName')
    first_name.type('Vitek')

    assert first_name == 'Vitek'
