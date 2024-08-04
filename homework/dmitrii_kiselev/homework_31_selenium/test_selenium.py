import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_1_demoblaze(driver):
    driver.get('https://www.demoblaze.com/index.html')
    driver.implicitly_wait(5)
    link = driver.find_element(By.LINK_TEXT, "Nexus 6")

    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    price = driver.find_element(By.CLASS_NAME, 'price-container').text.split()[0]

    to_cart_adding_button = driver.find_element(By.XPATH, "//a[@onclick='addToCart(3)']")
    to_cart_adding_button.click()

    WebDriverWait(driver, 10).until(ec.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    go_to_cart = driver.find_element(By.ID, 'cartur')
    go_to_cart.click()
    assert driver.find_element(By.XPATH, '//td[contains(text(),"Nexus 6")]')
    assert driver.find_element(By.ID, "totalp").text == price[1:]

    driver.quit()


def test_2_magento(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')

    first_bag = driver.find_element(By.XPATH, '//img[@class="product-image-photo"]')
    ActionChains(driver).move_to_element(first_bag).perform()

    name = driver.find_element(By.XPATH, '//a[@class="product-item-link"]').text

    add_to_compare = driver.find_element(By.XPATH, '//a[@title="Add to Compare"]')
    add_to_compare.click()

    assert driver.find_element(By.XPATH, '//a[@class="product-item-link"]').text == name

    driver.quit()


def test_3_qa_practice(driver):
    driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')

    launch_pop_up_button = driver.find_element(By.XPATH, '//button[contains(text(),"Launch Pop-Up")]')
    launch_pop_up_button.click()

    iframe = driver.find_element(By.XPATH, '//iframe')
    driver.switch_to.frame(iframe)
    found_text = driver.find_element(By.ID, 'text-to-copy').text
    driver.switch_to.default_content()

    check_button = driver.find_element(By.XPATH, '//button[contains(text(),"Check")]')
    check_button.click()

    check_input = driver.find_element(By.ID, 'id_text_from_iframe')
    check_input.send_keys(found_text)

    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()

    assert driver.find_element(By.ID, 'check-result').text == 'Correct!'

    driver.quit()
