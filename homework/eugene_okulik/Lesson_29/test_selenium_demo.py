from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    sleep(1)
    driver.quit()


def test_find_by_class(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    yoga_button = driver.find_element(By.CLASS_NAME, 'button')
    print(yoga_button.value_of_css_property('color'))
    yoga_button.click()


def test_search_field_css(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    search_field = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search entire store here..."]')
    # search_field = driver.find_element(By.CSS_SELECTOR, '#search')
    # search_field = driver.find_element(By.ID, 'search')
    # search_field = driver.find_element(By.NAME, 'q')
    # search_field = driver.find_element(By.CSS_SELECTOR, '[name="q"]')
    search_field.send_keys('man')
    search_field.submit()


def test_search_field_xpath(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    search_field = driver.find_element(By.XPATH, '//input[@placeholder="Search entire store here..."]')
    # search_field = driver.find_element(By.CSS_SELECTOR, '#search')
    # search_field = driver.find_element(By.ID, 'search')
    # search_field = driver.find_element(By.XPATH, '//*[@id="search"]')
    # search_field = driver.find_element(By.NAME, 'q')
    # search_field = driver.find_element(By.XPATH, '//*[@name="q"]')
    search_field.send_keys('man')
    search_field.submit()
