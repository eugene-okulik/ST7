from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/automation-practice-form")
driver.implicitly_wait(5)

driver.find_element(By.ID, "firstName").send_keys("Evgeny")
driver.find_element(By.ID, "lastName").send_keys("Shit")
driver.find_element(By.ID, "userEmail").send_keys("X0XUa@example.com")
driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]').click()
driver.find_element(By.ID, "userNumber").send_keys("9999998608")
driver.find_element(By.ID, "dateOfBirthInput").click()
driver.find_element(By.XPATH, '//option[text()="January"]').click()
driver.find_element(By.XPATH, '//option[text()="1990"]').click()
driver.find_element(By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--024"]').click()
driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
driver.find_element(By.XPATH, '//div[contains(@class, "subjects-auto-complete__menu")]').click()
driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-3"]').click()
driver.find_element(By.ID, "currentAddress").send_keys("some adress")
driver.find_element(By.XPATH, '(//*[@class=" css-1hwfws3"])[1]').click()
WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Uttar Pradesh')]"))
).click()
driver.find_element(By.XPATH, '(//*[@class=" css-1hwfws3"])[2]').click()
WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Merrut')]"))
).click()
driver.find_element(By.ID, "submit").click()
table = WebDriverWait(driver, 10).until(
    ec.visibility_of_element_located(
        (By.XPATH, '//*[@class="table table-dark table-striped table-bordered table-hover"]')))
print(table.text)
