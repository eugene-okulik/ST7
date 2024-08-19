from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    # driver.implicitly_wait(7)
    driver.maximize_window()
    yield driver
    # driver.quit()


def test_task1(driver):
    driver.get('https://www.demoblaze.com/index.html')
    driver.execute_script("window.scrollTo(0, 700)")
    wait = WebDriverWait(driver, 7)
    link_iphone6 = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, 'Iphone 6 32gb')))
    # link_iphone6 = driver.find_element(By.LINK_TEXT, 'Iphone 6 32gb')
    ActionChains(driver).key_down(Keys.CONTROL).click(link_iphone6).key_up(Keys.CONTROL).perform()
    new_page = driver.window_handles
    driver.switch_to.window(new_page[1])
    # sleep(9)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@class="btn btn-success btn-lg"]'))).click()
    # driver.find_element(By.XPATH, '//*[@class="btn btn-success btn-lg"]').click()
    # sleep(6)
    wait.until(ec.alert_is_present())
    driver.switch_to.alert.accept()
    driver.close()
    driver.switch_to.window(new_page[0])
    # sleep(7)
    # driver.find_element(By.XPATH, '//*[@id="cartur"]').click()
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="cartur"]'))).click()
    sleep(14)
    assert driver.find_element(By.XPATH, '//td[text()="Iphone 6 32gb"]').text == 'Iphone 6 32gb'


def test_card(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    # sleep(5)
    # card = driver.find_element(By.XPATH, '//img[@alt="Push It Messenger Bag"]')
    wait = WebDriverWait(driver, 6)
    card = wait.until(ec.visibility_of_element_located((By.XPATH, '//img[@alt="Push It Messenger Bag"]')))
    button_add_compare = driver.find_element(By.XPATH, '//a[@aria-label="Add to Compare"]')
    action = ActionChains(driver)
    action.move_to_element(card)
    action.click(button_add_compare).perform()
    compare_products = wait.until(ec.visibility_of_element_located((By.XPATH, '//strong[@class="product-item-name"]')))
    assert compare_products.text == 'Push It Messenger Bag'


def test_task3_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')
    driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()
    driver.switch_to.frame(0)
    text_copy = driver.find_element(By.XPATH, '//*[@id="text-to-copy"]').text
    driver.switch_to.default_content()
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    text_paste = driver.find_element(By.ID, 'id_text_from_iframe')
    text_paste.send_keys(text_copy)
    driver.find_element(By.ID, 'submit-id-submit').click()
    check_result = driver.find_element(By.ID, 'check-result')
    assert check_result.text == 'Correct!'
