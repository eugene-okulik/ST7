from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://www.qa-practice.com/elements/input/simple')
search_input = driver.find_element(By.ID, 'id_text_string')
search_input.send_keys('Kakoj-to_text')
sleep(2)
search_input.submit()
sleep(2)
response_text = driver.find_element(By.ID, 'result-text')
print(response_text.text)

driver.quit()
