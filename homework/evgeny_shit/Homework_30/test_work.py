from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)


def test_check_language():
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    select_element = driver.find_element(By.ID, 'id_choose_language')
    select = Select(select_element)
    select.select_by_value("1")
    select_element.submit()
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'result-text'))
    )
    assert "Python" in driver.find_element(By.ID, 'result-text').text


def test_check_country():
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    select_element = driver.find_element(By.XPATH, '//button[text()]')
    select_element.click()
    finish = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'finish'))
    )
    assert "Hello World!" in finish.text
