from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Firefox()
driver.maximize_window()


def find_by_class():
    driver.get('https://magento.softwaretestingboard.com/')
    yoga_button = driver.find_element(By.CLASS_NAME, 'button')
    yoga_button.click()
    sleep(3)  # для демонстрации


find_by_class()





driver.quit()