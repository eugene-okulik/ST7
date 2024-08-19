from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    choose_lang_dropdown = driver.find_element(By.NAME, 'choose_language')
    select = Select(choose_lang_dropdown)
    select.select_by_value("4")
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    result = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, "result"))).text
    assert "Java" in result


def test_hello_world(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.XPATH, '//button[text()]')
    start_button.click()
    finish = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "finish"))).text
    assert 'Hello World!' == finish
