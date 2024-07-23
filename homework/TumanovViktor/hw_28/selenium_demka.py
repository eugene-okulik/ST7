from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.set_window_size(1536, 731)
driver.get('https://www.qa-practice.com/elements/input/simple')
search_input = driver.find_element(By.ID, 'id_text_string')
search_input.send_keys('qa')
search_input.submit()
sleep(1)
search_result = driver.find_element(By.ID, 'result-text')
assert search_result.text == 'qa'
print('Текст который вы писали: ', search_result.text)
sleep(2)

button = driver.find_element(By.ID, 'req_header')
button.click()
sleep(4)

click_alerts = driver.find_element(By.PARTIAL_LINK_TEXT, 'Contact')
click_alerts.click()
sleep(3)

driver.close()
