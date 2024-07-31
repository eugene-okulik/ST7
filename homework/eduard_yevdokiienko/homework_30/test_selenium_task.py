from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    sleep(1)
    driver.quit()


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    choose_language_field = driver.find_element(By.XPATH, '//select[@id="id_choose_language"]')
    dropdown = Select(choose_language_field)
    dropdown.select_by_visible_text('Python')
    submit_button = driver.find_element(By.XPATH, '//input[@id="submit-id-submit"]')
    submit_button.click()
    req_text = driver.find_element(By.XPATH, '//p[@id="result-text"]')
    assert req_text.text == 'Python'


def test_hello_world(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.XPATH, '//button[contains(text(),"Start")]')
    start_button.click()
    req_text = driver.find_element(By.XPATH, '//div[@id="finish"]')
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable(req_text))
    assert req_text.text == 'Hello World!'
