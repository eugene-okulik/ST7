from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    sleep(1)
    driver.quit()


def test_first(driver):
    driver.get('https://www.demoblaze.com/index.html')
    nexus_6 = driver.find_element(By.XPATH, '//a[contains(text(),"Nexus 6")]')
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.click(nexus_6)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Add to cart")]')))
    driver.find_element(By.XPATH, '//a[contains(text(),"Add to cart")]').click()
    sleep(3)
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.XPATH, '//a[@id="cartur"]').click()
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, '//td[contains(text(),"Nexus 6")]')))
    assert driver.find_element(By.XPATH, '//td[contains(text(),"Nexus 6")]').text == 'Nexus 6'


def test_second(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    first_product = driver.find_element(By.XPATH, '//img[@alt = "Push It Messenger Bag"]')
    add_to_compare_button = driver.find_element(By.XPATH, '//a[@aria-label = "Add to Compare"]')
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)
    actions.move_to_element(first_product)
    actions.click(add_to_compare_button)
    actions.perform()
    compare_products = wait.until(ec.visibility_of_element_located((By.XPATH, '//strong[@class="product-item-name"]')))
    assert compare_products.text == 'Push It Messenger Bag'


def test_third(driver):
    driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, '//button[contains(text(), "Launch Pop-Up")]').click()
    driver.switch_to.frame(0)
    req_text = driver.find_element(By.XPATH, '//p[@id="text-to-copy"]').text
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, '//button[contains(text(), "Check")]').click()
    text_input = driver.find_element(By.XPATH, '//input[@name="text_from_iframe"]')
    text_input.send_keys(req_text)
    driver.find_element(By.XPATH, '//input[@id="submit-id-submit"]').click()
    result = wait.until(ec.visibility_of_element_located((By.XPATH, '//div[@id="check-result"]')))
    assert result.text == 'Correct!'
