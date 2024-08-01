from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_hello_world(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.CSS_SELECTOR, '.example #start')
    start_button.click()
    finish = WebDriverWait(driver, 5).until(ec.visibility_of_element_located(By.ID, 'final'))
    assert 'Hello World!' in finish.text
