from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()


def input_fields():
    driver.get('https://demoqa.com/automation-practice-form')
    driver.set_window_size(713, 729)
    sleep(2)
    field_first_name = driver.find_element(By.CSS_SELECTOR, '#firstName')
    field_first_name.send_keys('Paul')
    sleep(2)
    field_last_name = driver.find_element(By.CSS_SELECTOR, '#lastName')
    field_last_name.send_keys('Mauer')
    sleep(2)
    field_email = driver.find_element(By.CSS_SELECTOR, '#userEmail')
    field_email.send_keys('paulmauer@gmail.com')
    sleep(2)
    scroll = driver.find_element(By.CSS_SELECTOR, '#firstName')
    scroll.send_keys(Keys.PAGE_DOWN)
    sleep(1)
    radio_gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    radio_gender.click()
    sleep(2)
    field_number = driver.find_element(By.CSS_SELECTOR, '#userNumber')
    field_number.send_keys('7327899025')
    sleep(2)
    field_dob = driver.find_element(By.ID, 'dateOfBirthInput')
    field_dob.click()
    field_dob.send_keys(Keys.CONTROL + 'a')
    field_dob.send_keys('05 Feb 1985')
    field_dob.send_keys(Keys.ENTER)
    sleep(2)
    field_subject = driver.find_element(By.ID, 'subjectsInput')
    field_subject.send_keys('so')
    sleep(2)
    select_subject = driver.find_element(By.CSS_SELECTOR, '#react-select-2-option-0')
    select_subject.click()
    sleep(2)
    field_hobby = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-3']")
    field_hobby.click()
    sleep(2)
    field_address = driver.find_element(By.ID, 'currentAddress')
    field_address.send_keys('Princeton, NJ 08000')
    sleep(2)
    field_state = driver.find_element(By.ID, 'react-select-3-input')
    field_state.send_keys('haryana')
    field_state.send_keys(Keys.ENTER)
    sleep(2)
    field_city = driver.find_element(By.ID, 'react-select-4-input')
    field_city.send_keys('panipat')
    field_city.send_keys(Keys.ENTER)
    sleep(2)
    field_submit = driver.find_element(By.ID, 'submit')
    field_submit.click()
    sleep(2)
    final_form = driver.find_element(
        By.XPATH, "//*[@class='table table-dark table-striped table-bordered table-hover']"
    )
    print(final_form.text)


input_fields()
driver.quit()
