from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_qa_practice():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    choose_language = driver.find_element(By.ID, 'id_choose_language')
    language_choice = driver.find_element(By.XPATH, '//option[@value="1"]').text
    dropdown = Select(choose_language)
    dropdown.select_by_value('1')

    submit_button = driver.find_element(By.ID, "submit-id-submit")
    submit_button.click()
    submitted_text = driver.find_element(By.ID, "result-text")
    assert submitted_text.text == language_choice

    driver.quit()


def test_herokuapp():
    driver = webdriver.Firefox()
    # driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    start_button = driver.find_element(By.XPATH, '//button[contains(text(),"Start")]')
    start_button.click()
    # finish_text = driver.find_element(By.XPATH, '//h4[contains(text(),"Hello World!")]')
    wait = WebDriverWait(driver, 20)
    finish_text = wait.until(ec.element_to_be_clickable((By.XPATH, '//h4[contains(text(),"Hello World!")]')))
    assert finish_text

    driver.quit()
