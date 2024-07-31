from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    # driver.quit()


def test_task1(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_choose = driver.find_element(By.ID, 'id_choose_language')
    driver.implicitly_wait(3)
    select_choose.click()
    select_choose.find_element(By.XPATH, '//*[@value="1"]').click()

    click_button_submit = driver.find_element(By.ID, 'submit-id-submit')
    click_button_submit.click()

    result_text = driver.find_element(By. ID, 'result-text')
    # print(result_text.text)
    assert result_text.text == 'Python'


def test_task2(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    # driver.find_element(By.TAG_NAME, 'button').click()  # находим кнопку и кликаем
    driver.find_element(By.XPATH, '//button[contains(text(),"Start")]').click()    # Вариант более надёжный
    driver.implicitly_wait(5)
    finish = driver.find_element(By.ID, 'finish')
    # print(finish.text)
    assert finish.text == 'Hello World!'
