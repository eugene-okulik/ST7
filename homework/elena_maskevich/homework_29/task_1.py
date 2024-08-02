import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(912, 1200)
    yield driver
    driver.quit()


def test_form_page(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    name_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="First Name"]')
    name_input.send_keys('Alena')
    last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
    last_name_input.send_keys('Maskevich')
    email_input = driver.find_element(By.CSS_SELECTOR, '#userEmail')
    email_input.send_keys('maskevich@mail.ru')
    gender_radiobutton = driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-2"]')
    gender_radiobutton.click()
    mobile_input = driver.find_element(By.XPATH, '//*[@id="userNumber"]')
    mobile_input.send_keys('1112223334')
    date_input = driver.find_element(By.XPATH, '//*[@id="dateOfBirthInput"]')
    date_input.click()
    month_select = driver.find_element(By.XPATH, '//*[@class="react-datepicker__month-select"]')
    month_input = Select(month_select)
    month_input.select_by_value('5')
    year_select = driver.find_element(By.XPATH, '//*[@class="react-datepicker__year-select"]')
    year_input = Select(year_select)
    year_input.select_by_value('1905')
    driver.implicitly_wait(3)
    driver.execute_script("window.scrollTo(0, 500)")
    subject_input = driver.find_element(By.CSS_SELECTOR, '#subjectsInput')
    subject_input.send_keys('en')
    subject_selected = driver.find_element(By.CSS_SELECTOR, '#react-select-2-option-0')
    subject_selected.click()
    hobbies_checkbox_1 = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    hobbies_checkbox_1.click()
    address_input = driver.find_element(By.CSS_SELECTOR, '#currentAddress')
    address_input.send_keys('Minsk')
    state_input = driver.find_element(By.XPATH, '//div[contains(text(),"Select State")]')
    state_input.click()
    state = driver.find_element(By.CSS_SELECTOR, '#react-select-3-option-2')
    state.click()
    time.sleep(3)
    city_input = driver.find_element(By.CSS_SELECTOR, '#city')
    city_input.click()
    city = driver.find_element(By.CSS_SELECTOR, '#react-select-4-option-1')
    city.click()
    submit_input = driver.find_element(By.CSS_SELECTOR, '#submit')
    submit_input.click()
    submitted_form = driver.find_element(By.CSS_SELECTOR, '#example-modal-sizes-title-lg')
    print(submitted_form.text)
