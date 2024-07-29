from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.set_window_size(1920, 1080)
driver.get("https://demoqa.com/automation-practice-form")
driver.implicitly_wait(5)

first_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'firstName')))
first_name.send_keys('Alex_AQA')
last_name = driver.find_element(By.ID, 'lastName')
last_name.send_keys('Seniorovich')
email = driver.find_element(By.ID, 'userEmail')
email.send_keys('test@tut.by')
gender_radio_button = driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
gender_radio_button.click()
mobile_number = driver.find_element(By.ID, 'userNumber')
mobile_number.send_keys('1234567890')
date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
date_of_birth.click()
wait.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'react-datepicker__month')))
date_of_birth.send_keys(Keys.CONTROL + "a")
date_of_birth.send_keys('01012000')
date_of_birth.send_keys(Keys.ENTER)
subjects = driver.find_element(By.ID, 'subjectsInput')
driver.execute_script("arguments[0].scrollIntoView();", subjects)
subjects.click()
subjects.send_keys('en')
english = wait.WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, 'react-select-2-option-0')))
english.click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[text()='English']")))
wait.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//label[@for="hobbies-checkbox-1"]')))
hobbies = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
hobbies.click()
address = driver.find_element(By.ID, 'currentAddress')
address.send_keys('Baker str')
state = driver.find_element(By.ID, 'react-select-3-input')
state.send_keys('NCR')
state.send_keys(Keys.ENTER)
city = driver.find_element(By.ID, 'react-select-4-input')
city.send_keys('Delhi')
city.send_keys(Keys.ENTER)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
submit_button = driver.find_element(By.XPATH, '//*[@id="submit"]')
submit_button.click()
info = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '//*[@class="table table-dark table-striped table-bordered table-hover"]'))).text
print(info)
driver.quit()
