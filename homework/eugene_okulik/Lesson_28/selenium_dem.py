from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Firefox()
driver.maximize_window()


def google():
    driver.get('https://www.google.com/')
    # search_input = driver.find_element(By.NAME, 'q')
    search_input = driver.find_element(By.ID, 'APjFqb')
    search_input.send_keys('cat')
    sleep(1)
    # search_input.submit()
    search_input.send_keys(Keys.ENTER)
    # button = driver.find_element(By.NAME, 'btnK')
    # button.click()
    sleep(1)
    assert driver.title.startswith('cat')
    assert 'q=cat' in driver.current_url
    links = driver.find_elements(By.CSS_SELECTOR, '[jsname="UWckNb"]')
    links[0].click()
    sleep(3)


def simple():
    driver.get('https://magento.softwaretestingboard.com/sale.html')
    header = driver.find_element(By.TAG_NAME, 'h1')
    assert header.text == 'Sale'
    search_terms = driver.find_element(By.PARTIAL_LINK_TEXT, 'Search Te')
    search_terms.click()
    sleep(3)


google()
driver.quit()
