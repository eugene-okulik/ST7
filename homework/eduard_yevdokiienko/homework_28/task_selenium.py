from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()


driver.get('https://www.qa-practice.com/elements/input/simple')
text_string = driver.find_element(By.XPATH, "//input[@id='id_text_string']")
text_string.send_keys('error')
text_string.submit()
find_element = driver.find_element(By.XPATH, "//p[@id='result-text']")
assert find_element.text == 'error'
print('Searched text: ', find_element.text)
sleep(2)

buttons = driver.find_element(By.XPATH, "//a[contains(text(),'Buttons')]")
buttons.click()
button_click = driver.find_element(By.XPATH, "//input[@id='submit-id-submit']")
button_click.click()
result_text = driver.find_element(By.XPATH, "//p[@id='result-text']")
assert result_text.text == 'Submitted'
print('Searched text: ', result_text.text)
sleep(2)


driver.quit()
