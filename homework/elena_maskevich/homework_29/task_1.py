import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
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
    month_input = driver.find_element(By.XPATH, '//*[@class="react-datepicker__month-select"]')
    month_input.click()
    month_selected = driver.find_element(By.XPATH, '//option[@value="5"]')
    month_selected.click()
    year_select = driver.find_element(By.XPATH, '//*[@react-datepicker__year-select"]')
    year_select.click()
    year_selected = driver.find_element(By.XPATH, '//option[@value="1905"]')
    year_selected.click()
    subject_input = driver.find_element(By.CSS_SELECTOR, '#subjectsInput')
    subject_input.send_keys('math, chemistry, informatics')
    hobbies_checkbox_1 = driver.find_element(By.CSS_SELECTOR, '#hobbies-checkbox-1')
    hobbies_checkbox_1.click()
    address_input = driver.find_element(By.CSS_SELECTOR, 'currentAddress')
    address_input.send_keys('Minsk')
    state_input = driver.find_element(By.XPATH, '//div[contains(text(),"Select State")]')


    time.sleep(3)
# search_input.send_keys('hello')
# search_input.submit()
# time.sleep(3)
# result_text = driver.find_element(By.ID, 'result-text')
# assert result_text.text == 'hello'
