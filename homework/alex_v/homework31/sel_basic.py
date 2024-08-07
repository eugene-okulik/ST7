import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_mobile_phone_cart_adding(driver):
    driver.get("https://www.demoblaze.com/index.html")
    phone = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Iphone 6 32gb")))
    phone.send_keys(Keys.CONTROL + Keys.RETURN)
    driver.switch_to.window(driver.window_handles[1])
    add_to_cart = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))
    )
    add_to_cart.click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cartur"))
    )
    cart.click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Iphone 6 32gb')]"))
    )

    phone_cart = driver.find_element(By.XPATH, "//td[contains(text(), 'Iphone 6 32gb')]").text
    assert "Iphone 6 32gb" in phone_cart


def test_item_comparing(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    first_product = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(@class,'product-item')][1]"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(first_product).perform()
    add_to_compare_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Add to Compare']"))
    )
    add_to_compare_button.click()
    compare_product_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item-name"))
    )
    assert "Push It Messenger Bag" in compare_product_name.text


def test_pop_up(driver):
    driver.get("https://www.qa-practice.com/elements/popup/iframe_popup")
    driver.find_element(By.XPATH, '//button[contains(text(), "Launch Pop-Up")]').click()
    driver.switch_to.frame(0)
    text = driver.find_element(By.XPATH, '//p[@id="text-to-copy"]').text
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, '//button[contains(text(), "Check")]').click()
    text_input = driver.find_element(By.XPATH, '//input[@name="text_from_iframe"]')
    text_input.send_keys(text)
    driver.find_element(By.XPATH, '//input[@id="submit-id-submit"]').click()
    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@id="check-result"]'))).text
    assert result == 'Correct!'
