from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_ui_framework():
    expected_text = "java_rules"
    driver.get('https://www.qa-practice.com/elements/input/simple')
    search_input = driver.find_element(By.XPATH, "//input[@type='text']")
    search_input.click()
    search_input.send_keys(expected_text)
    driver.implicitly_wait(3)
    search_input.submit()
    driver.implicitly_wait(1)
    result_pop_up_text = driver.find_element(By.XPATH, "//input[@type='text']").text
    assert result_pop_up_text == expected_text
    driver.close()
    driver.quit()
