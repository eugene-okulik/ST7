import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.qa-practice.com/elements/input/simple')
time.sleep(3)
search_input = driver.find_element(By.NAME, 'text_string')
search_input.send_keys('hello')
search_input.submit()
time.sleep(3)
result_text = driver.find_element(By.ID, 'result-text')
assert result_text.text == 'hello'
driver.quit()
