import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
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
