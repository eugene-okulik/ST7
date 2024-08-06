from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
import custom_waits


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    sleep(1)
    driver.quit()


def test_cookies(driver):
    driver.get('https://www.demoblaze.com/index.html')
    # sleep(3)
    WebDriverWait(driver, 5).until(custom_waits.cookies_not_empty(driver))
    print(driver.get_cookies())
    driver.add_cookie({'name': 'test', 'value': "AAAAAAAAAAAAAAAAAAAAAAAAAA"})
    print(driver.get_cookies())


def test_men(driver):
    driver.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    men = driver.find_elements(By.CSS_SELECTOR, '[data-container="product-grid"]')
    for man in men:
        print(man.find_element(By.CLASS_NAME, 'price').text)
    prices = list(map(lambda elt: elt.find_element(By.CLASS_NAME, 'price').text, men))
    print(prices)


def test_tabs(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    driver.find_element(By.ID, 'new-page-link').click()
    tabs = driver.window_handles  # ['ksjdhf-sdkfjhsd-sdkfjhsdf', 'skdjfksdf-weiuywe-jsdhf']
    driver.switch_to.window(tabs[1])
    assert driver.find_element(By.ID, 'result-text').text == 'I am a new page in a new tab'
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.ID, 'new-page-link').click()


def test_stale_element(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    button = driver.find_element(By.ID, 'submit-id-submit')
    checkbox.click()
    button.click()
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    checkbox.click()


def test_iframes(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.XPATH, '//iframe')
    driver.switch_to.frame(iframe)
    driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon').click()
    sleep(1)
    driver.switch_to.default_content()


def test_alert(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element(By.CLASS_NAME, 'a-button').click()
    alert = Alert(driver)
    alert.accept()
    sleep(1)


def test_hover(driver):
    driver.get('https://magento.softwaretestingboard.com/men.html')
    men = driver.find_element(By.ID, 'ui-id-5')
    tops = driver.find_element(By.ID, 'ui-id-17')
    jackets = driver.find_element(By.ID, 'ui-id-19')
    # ActionChains(driver).move_to_element(men).move_to_element(tops).click(jackets).perform()
    sleep(3)
    actions = ActionChains(driver)
    actions.move_to_element(men)
    actions.move_to_element(tops)
    # wait
    actions.click(jackets)
    actions.perform()


def test_key_down(driver):
    driver.get('https://www.qa-practice.com/')
    link = driver.find_element(By.LINK_TEXT, 'Homepage')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    sleep(3)


def test_dnd(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_me = driver.find_element(By.ID, 'rect-draggable')
    drop_here = driver.find_element(By.ID, 'rect-droppable')
    # ActionChains(driver).drag_and_drop(drag_me, drop_here).perform()
    actions = ActionChains(driver)
    actions.move_to_element(drag_me)
    actions.click_and_hold()
    actions.move_to_element(drop_here)
    actions.release()
    actions.perform()
    sleep(3)


def test_price(driver):
    driver.get('https://sreda.ru/flats')
    bubble = driver.find_element(By.CSS_SELECTOR, '[data-slot="thumb"]')
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(bubble, 70, 0)
    actions.perform()
    sleep(3)


def test_upload(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    file_upload = driver.find_element(By.ID, 'file-upload')
    file_upload.send_keys('/home/eugene/Downloads/vacation.png')
    sleep(3)
