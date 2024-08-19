import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_page(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start = driver.find_element(By.XPATH, '//button')
    start.click()
    driver.implicitly_wait(7)
    finish = driver.find_element(By.XPATH, '//div[@id="finish"]')
    assert finish.text == 'Hello World!'
