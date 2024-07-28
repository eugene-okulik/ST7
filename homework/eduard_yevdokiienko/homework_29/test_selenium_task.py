from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    sleep(3)
    driver.quit()


def test_fill_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name_input = driver.find_element(By.XPATH, '//input[@id="firstName"]')
    first_name_input.send_keys('eduard')
    last_name_input = driver.find_element(By.XPATH, '//input[@id="lastName"]')
    last_name_input.send_keys('y')
    email_input = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
    email_input.send_keys('eduard@email.com')
    gender_radio_label = driver.find_element(By.XPATH, '//label[contains(text(),"Male")]')
    gender_radio_label.click()
    mobile_number_input = driver.find_element(By.XPATH, '//input[@id="userNumber"]')
    mobile_number_input.send_keys('0123456789')
    date_of_birth_input = driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]')
    date_of_birth_input.click()
    month_select = driver.find_element(By.XPATH, '//option[contains(text(),"April")]')
    month_select.click()
    year_select = driver.find_element(By.XPATH, '//option[contains(text(),"1991")]')
    year_select.click()
    day_select = driver.find_element(By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--005"]')
    day_select.click()
    subject_input = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    subject_input.send_keys('Math')
    subject_auto_complete = driver.find_element(By.XPATH, '//div[contains(@class, "subjects-auto-complete__menu")]')
    subject_auto_complete.click()
    hobbies_checkbox = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    hobbies_checkbox.click()
    current_address_textarea = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
    current_address_textarea.send_keys('current address')
    select_state = driver.find_element(By.XPATH, '//div[contains(text(),"Select State")]')
    select_state.click()
    choose_state = driver.find_element(By.XPATH, '//*[contains(text(), "NCR")]')
    choose_state.click()
    select_city = driver.find_element(By.XPATH, '//div[contains(text(),"Select City")]')
    select_city.click()
    choose_city = driver.find_element(By.XPATH, '//*[contains(text(), "Delhi")]')
    choose_city.click()
    submit_button = driver.find_element(By.XPATH, '//button[@id="submit"]')
    submit_button.click()
    sleep(3)

    table = driver.find_element(
        By.XPATH, '//table[@class = "table table-dark table-striped table-bordered table-hover"]'
    )
    print(table.text)
