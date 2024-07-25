from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://www.qa-practice.com/elements/input/simple')
text_string = driver.find_element(By.ID, 'id_text_string')
sleep(1)
text_string.send_keys('qa')
text_string.submit()
sleep(2)

result_text = driver.find_element(By.ID, 'result-text')
assert result_text.text == 'qa'
print('Текст который вы писали: ', result_text.text)
sleep(2)

dropdown_trigger = driver.find_element(By.ID, 'req_header')
dropdown_trigger.click()
sleep(3)

click_concat_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Contact')
click_concat_link.click()
sleep(2)

driver.close()
