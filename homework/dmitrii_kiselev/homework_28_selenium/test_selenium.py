from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_demoqa():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get('https://demoqa.com/automation-practice-form')

    input_name = driver.find_element(By.ID, 'firstName')
    input_name.send_keys('Dmitrii')

    input_lastname = driver.find_element(By.ID, 'lastName')
    input_lastname.send_keys('Kiselev')

    input_email = driver.find_element(By.ID, 'userEmail')
    input_email.send_keys('didroi@yandex.ru')

    gender_radio_button = driver.find_element(By.XPATH, '//label[@class="custom-control-label"]')
    gender_radio_button.click()

    input_phone = driver.find_element(By.ID, 'userNumber')
    input_phone.send_keys('4207742432')

    input_birth_date = driver.find_element(By.ID, 'dateOfBirthInput')
    for _ in range(len(input_birth_date.get_attribute('value'))-1):
        input_birth_date.send_keys(Keys.BACKSPACE)
    input_birth_date.send_keys(Keys.ARROW_LEFT)
    input_birth_date.send_keys('09.01.1983')
    input_birth_date.send_keys(Keys.DELETE)
    input_birth_date.send_keys(Keys.ENTER)

    input_autocomplete = driver.find_element(By.ID, 'subjectsInput')
    input_autocomplete.send_keys('e')
    driver.execute_script("window.scrollTo(0, 400)")
    dropdown_autocomplete = driver.find_element(By.ID, "react-select-2-option-2")
    dropdown_autocomplete.click()

    hobbies_checkbox = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    hobbies_checkbox.click()

    image_upload_button = driver.find_element(By.ID, 'uploadPicture')  # А как это сделать?

    address_text_area = driver.find_element(By.ID, 'currentAddress')
    address_text_area.send_keys("False address")

    driver.execute_script("window.scrollTo(0, 400)")  # Ну он продолжает у меня отскакивать!

    state_select = driver.find_element(By.ID, "state")
    state_select.click()
    state_select_choose = driver.find_element(By.ID, "react-select-3-option-2")
    state_select_choose.click()

    city_select = driver.find_element(By.ID, "city")
    city_select.click()
    city_select_choose = driver.find_element(By.ID, "react-select-4-option-1")
    city_select_choose.click()

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    submitting_modal = driver.find_element(By.ID, "example-modal-sizes-title-lg")
    assert submitting_modal.text == 'Thanks for submitting the form'

    driver.quit()
