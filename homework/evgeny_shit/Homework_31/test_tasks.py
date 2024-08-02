from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)


def test_first():
    driver.get("https://www.demoblaze.com/index.html")
    card_nokia = driver.find_element(By.XPATH, '//div[@class="card h-100"]/a[@href="prod.html?idp_=2"]')
    href = card_nokia.get_attribute("href")
    driver.execute_script(f"window.open('{href}', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//a[text()="Add to cart"]'))
    ).click()
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    driver.switch_to.alert.accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, 'cartur').click()
    goods = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, '//td[text()="Nokia lumia 1520"]'))
    )
    assert "Nokia lumia 1520" in goods.text


def test_second():
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    card = driver.find_element(By.XPATH, '(//*[@class="product-item-info"])[1]')
    ActionChains(driver).move_to_element(card).click(
        card.find_element(By.XPATH, '//*[@class="action tocompare"]')).perform()
    compare_items = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'compare-items'))
    )
    assert "Push It Messenger Bag" in compare_items.text


def test_third():
    driver.get("https://www.qa-practice.com/elements/popup/iframe_popup")
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, '//button[normalize-space(text())="Launch Pop-Up"]'))
    ).click()
    driver.switch_to.frame(0)
    copy_text = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'text-to-copy'))
    ).text
    driver.switch_to.default_content()
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    input_str = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'id_text_from_iframe'))
    )
    input_str.send_keys(copy_text)
    input_str.submit()
    result = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'check-result'))
    )
    assert "Correct!" in result.text
