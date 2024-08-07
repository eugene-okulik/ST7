from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_item(driver):
    driver.get('https://www.demoblaze.com/index.html')
    item = driver.find_element(By.XPATH, "//a[text()='Sony xperia z5']")
    ActionChains(driver).key_down(Keys.CONTROL).click(item).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart = driver.find_element(By.XPATH, '//a[text()="Add to cart"]').click()
    WebDriverWait(driver, 5).until(ec.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(By.ID, 'cartur').click()
    assert 'Sony xperia z5' in driver.find_element(By.CSS_SELECTOR, '.success').text


def test_compare(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    wait = WebDriverWait(driver, 8)
    tote = wait.until(ec.presence_of_element_located((By.XPATH, '//img[@alt="Compete Track Tote"]')))
    actions = ActionChains(driver)
    actions.move_to_element(tote).perform()
    compare_icon = wait.until(ec.visibility_of_element_located((
        By.XPATH, '(//a[@class="action tocompare" and @title="Add to Compare"])[6]'
    )))
    compare_icon.click()
    compare_products = wait.until(ec.visibility_of_element_located((
        By.XPATH, '//strong[@class="product-item-name"]'
    )))
    assert compare_products.text == 'Compete Track Tote'


def test_pop_up(driver):
    driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')
    pop_up_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary" and @data-bs-toggle="modal"]')
    pop_up_button.click()
    copy_from_iframe = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, '//iframe')))
    driver.switch_to.frame(copy_from_iframe)
    copy_text = driver.find_element(By.ID, 'text-to-copy').text
    driver.switch_to.default_content()
    close_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary" and @type="submit"]').click()
    input_field = driver.find_element(By.ID, 'id_text_from_iframe')
    input_field.send_keys(copy_text)
    input_field.submit()
    correct_button = driver.find_element(By.ID, 'check-result')
    assert correct_button.text == 'Correct!'
