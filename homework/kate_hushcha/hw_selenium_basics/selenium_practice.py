from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()


def web_homework():
    driver.get('https://www.qa-practice.com/elements/input/simple')
    sleep(1)
    input_field = driver.find_element(By.NAME, 'text_string')
    input_field.send_keys('mushroom')
    input_field.send_keys(Keys.ENTER)
    sleep(1)
    input_text = driver.find_element(By.ID, 'result-text')
    assert input_text.text == 'mushroom'
    print(input_text.text)


web_homework()
