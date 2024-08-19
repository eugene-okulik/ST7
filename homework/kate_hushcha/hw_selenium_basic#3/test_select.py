from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_select_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_input = driver.find_element(By.CSS_SELECTOR, '#id_choose_language')
    select_input.click()
    language_select = Select(select_input)
    language_select.select_by_visible_text('Ruby')
    submit_button = driver.find_element(By.CSS_SELECTOR, '#submit-id-submit')
    submit_button.click()
    result_button = driver.find_element(By.ID, 'result')
    assert 'Ruby' in result_button.text
