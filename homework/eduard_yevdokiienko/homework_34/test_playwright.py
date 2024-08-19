from playwright.sync_api import Page, expect


def test_first(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button_red = page.locator('//button[@class="mt-4 text-danger btn btn-primary"]')
    expect(button_red).to_be_enabled()
    button_red.click()


def test_second(page: Page):
    page.goto('https://demoqa.com/automation-practice-form ')
    page.locator('//input[@id="firstName"]').fill('eduard')
    page.locator('//input[@id="lastName"]').fill('y')
    page.locator('//input[@id="userEmail"]').fill('eduard@gmail.com')
    checkbox_gender = page.locator('//label[contains(text(),"Male")]')
    checkbox_gender.click()
    page.locator('//input[@id="userNumber"]').fill('0123456789')
    date_of_birth = page.locator('//input[@id="dateOfBirthInput"]')
    date_of_birth.click()
    month_selector = page.locator('//select[@class="react-datepicker__month-select"]')
    month_selector.select_option('3')
    year_selector = page.locator('//select[@class="react-datepicker__year-select"]')
    year_selector.select_option('1991')
    day_select = page.locator('//div[@class="react-datepicker__day react-datepicker__day--005"]')
    day_select.click()
    subject = page.locator('//input[@id="subjectsInput"]')
    subject.type('eng')
    subject.press('Enter')
    page.locator('//label[contains(text(),"Sports")]').click()
    page.locator('//textarea[@id="currentAddress"]').fill('adress')
    state = page.locator('//input[@id="react-select-3-input"]')
    state.type('Rajasth')
    state.press('Enter')
    city = page.locator('//input[@id="react-select-4-input"]')
    city.type('Jaip')
    city.press('Enter')
    page.locator('//button[@id="submit"]').click()

    student_name = page.locator('//td[contains(text(),"eduard y")]')
    expect(student_name).to_have_text('eduard y')
