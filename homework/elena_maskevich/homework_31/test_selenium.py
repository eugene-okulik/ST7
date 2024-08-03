import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_mobile_tabs(driver):
    driver.get('https://www.demoblaze.com/index.html')
    product_phone = driver.find_element(By.XPATH, '//a[contains(text(),"Samsung galaxy s6")]')
    ActionChains(driver).key_down(Keys.CONTROL).click(product_phone).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_card = driver.find_element(By.CSS_SELECTOR, "a[onclick='addToCart(1)']")
    add_to_card.click()
    WebDriverWait(driver, 5).until(ec.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.switch_to.default_content()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(By.CSS_SELECTOR, '#cartur')
    cart.click()
    assert driver.find_element(By.XPATH, '//td[contains(text(),"Samsung galaxy s6")]').text == "Samsung galaxy s6"


def test_hover_products_to_compare(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    product = driver.find_element(By.XPATH, '(//img[@class="product-image-photo"])[1]')
    name_of_added_product = product.get_attribute('alt')
    compare = driver.find_element(By.XPATH, '(//a[@title="Add to Compare"])[1]')
    actions=ActionChains(driver)
    actions.move_to_element(product)
    actions.click(compare)
    actions.perform()
    compared_product = driver.find_element(By.XPATH,'//strong[@class="product-item-name"]/a')
    assert compared_product.text == name_of_added_product


def test_iframes(driver):
    driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')
    launch_button = driver.find_element(By.XPATH, '//button[contains(text(),"Launch Pop-Up")]')
    launch_button.click()
    iframe = driver.find_element(By.XPATH, '//iframe')
    driver.switch_to.frame(iframe)
    copy_text = driver.find_element(By.CSS_SELECTOR, '#text-to-copy')
    copied_text = copy_text.get_attribute('innerText')
    driver.switch_to.default_content()
    check_button = driver.find_element(By.XPATH, '//button[@form="empty-form"]')
    check_button.click()
    text_from_frame = driver.find_element(By.ID, 'id_text_from_iframe')
    text_from_frame.send_keys(copied_text)
    submit_button = driver.find_element(By.CSS_SELECTOR,'#submit-id-submit')
    submit_button.click()
    output = driver.find_element(By.ID, 'check-result')
    assert output.get_attribute('innerText') == 'Correct!'
