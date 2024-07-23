from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()


driver.get('https://www.qa-practice.com/elements/input/simple')
search_input = driver.find_element(By.XPATH, "//input[@id='id_text_string']")
search_input.send_keys('error')
search_input.submit()
search_element = driver.find_element(By.XPATH, "//p[@id='result-text']")
assert search_element.text == 'error'
print('Searched text: ', search_element.text)
sleep(2)

buttons = driver.find_element(By.XPATH, "//a[contains(text(),'Buttons')]")
buttons.click()
button_click = driver.find_element(By.XPATH, "//input[@id='submit-id-submit']")
button_click.click()
submitted_element = driver.find_element(By.XPATH, "//p[@id='result-text']")
assert submitted_element.text == 'Submitted'
print('Searched text: ', submitted_element.text)
sleep(2)


driver.quit()
