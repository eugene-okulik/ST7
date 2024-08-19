from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    # driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    sleep(1)
    driver.quit()


def test_attributes(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input_label = driver.find_element(By.CSS_SELECTOR, '[for="id_text_string"]')
    print(input_label.get_attribute('class'))
    print(input_label.get_attribute('innerText'))
    collapsible = driver.find_element("css selector", '#req_text')
    print(collapsible.get_attribute('innerHTML'))
    text_string = driver.find_element(By.CSS_SELECTOR, '#id_text_string')
    text_string.send_keys('QWWER')
    print(text_string.get_attribute('value'))
    sleep(3)
    # text_string.clear()
    # for _ in text_string.get_attribute('value'):
    #     text_string.send_keys(Keys.BACKSPACE)
    text_string.send_keys(Keys.CONTROL + 'a')
    text_string.send_keys(Keys.BACKSPACE)

    sleep(5)


def test_enabled(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = driver.find_element(By.ID, 'submit-id-submit')
    sleep(1.5)
    assert not button.is_enabled(), 'Button is enabled'
    select_element = driver.find_element(By.ID, 'id_select_state')
    dropdown = Select(select_element)
    dropdown.select_by_visible_text('Enabled')
    sleep(1.5)
    assert button.is_enabled()
    dropdown.select_by_visible_text('Disabled')
    sleep(1.5)
    assert not button.is_enabled(), 'Button is enabled'
    req_header = driver.find_element(By.ID, 'req_header')
    req_text = driver.find_element(By.ID, 'req_text')
    assert not req_text.is_displayed()
    req_header.click()
    assert req_text.is_displayed()


def test_input(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.CSS_SELECTOR, '#id_text_string')
    text_string.send_keys('QWWER')
    text_string.submit()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == 'QWWER'


def test_wait_enabled(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    # button = driver.find_element(By.ID, 'enableAfter')
    # WebDriverWait(driver, 5).until(ec.element_to_be_clickable(button))
    button = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.ID, 'enableAfter')))
    button.click()
    # driver.execute_script("window.scrollTo(0, 300)")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(3)
