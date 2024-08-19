import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_page(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_language = driver.find_element(By.CSS_SELECTOR, '#id_choose_language')
    language = Select(select_language)
    language.select_by_value('5')
    submit = driver.find_element(By.CSS_SELECTOR, '#submit-id-submit')
    submit.click()
    result_submit = driver.find_element(By.ID, 'result-text')
    assert result_submit.text == 'C#'
