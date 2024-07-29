from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    sleep(1)
    driver.quit()


def test_form_filling(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name = driver.find_element(By.CSS_SELECTOR, '#firstName')
    first_name.send_keys('Vitek')
    sleep(1)

    last_name = driver.find_element(By.CSS_SELECTOR, '#lastName')
    last_name.send_keys('Tuman')
    sleep(1)

    user_email = driver.find_element(By.ID, 'userEmail')
    user_email.send_keys('pum@purum.com')
    sleep(1)

    driver.find_element(By.XPATH, '//label[@for="gender-radio-3"]').click()

    user_number = driver.find_element(By.XPATH, '//*[@id="userNumber"]')
    user_number.send_keys('79009000000')
    sleep(1)

    dropdown_data_birtch = driver.find_element(By.ID, 'dateOfBirthInput')
    dropdown_data_birtch.click()
    birth_data = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    birth_data.click()
    birth_year = driver.find_element(By.XPATH, '//*[@value="1993"]')
    birth_year.click()
    month = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    month.click()
    month = driver.find_element(By.XPATH, '//*[@value="7"]')
    month.click()
    day = driver.find_element(By.XPATH, '//*[@class="react-datepicker__day react-datepicker__day--023"]')
    day.click()
    sleep(1)

    subject_container = driver.find_element(By.XPATH, '//*[@id="subjectsInput"]')
    subject_container.send_keys('test text')
    subject_container = driver.find_element(By.XPATH, '//div[contains(@class, "subjects-auto-complete__menu")]')
    subject_container.click()
    sleep(1)

    box = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    box.click()

    current_text_address = driver.find_element(By.XPATH, '//*[@id="currentAddress"]')
    current_text_address.send_keys('Moscow, tverskay 14/b')
    sleep(1)

    select_state_drop = driver.find_element(By.XPATH, '//*[@id="react-select-3-input"]')
    select_state_drop.send_keys('NCR')
    select_state_drop.send_keys(Keys.ENTER)
    sleep(1)
    city = driver.find_element(By.XPATH, '//*[@id="react-select-4-input"]')
    city.send_keys('Delhi')
    city.send_keys(Keys.ENTER)
    sleep(1)

    driver.find_element(By.ID, 'submit').click()

    table = driver.find_element(By.XPATH,
                                '//*[@class="table table-dark table-striped table-bordered table-hover"]')
    print(table.text)
