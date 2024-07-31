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
    driver.maximize_window()
    yield driver
    driver.quit()


def test_task1(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_choose = driver.find_element(By.XPATH, '//select[@id="id_choose_language"]')
    driver.implicitly_wait(3)
    dropdown = Select(select_choose)
    dropdown.select_by_visible_text('Ruby')
    # select_choose.find_element(By.XPATH, '//*[@value="1"]').click()
    driver.find_element(By.ID, 'submit-id-submit').click()

    result_text = driver.find_element(By. ID, 'result-text')
    # print(result_text.text)
    assert result_text.text == 'Ruby'


def test_task2(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    # driver.find_element(By.TAG_NAME, 'button').click()  # находим кнопку и кликаем
    driver.find_element(By.XPATH, '//button[contains(text(),"Start")]').click()    # Вариант более надёжный
    driver.implicitly_wait(5)
    finish = driver.find_element(By.ID, 'finish')
    # print(finish.text)
    assert finish.text == 'Hello World!'
