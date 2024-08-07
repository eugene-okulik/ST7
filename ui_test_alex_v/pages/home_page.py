import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open the homepage')
    def open_site(self):
        self.driver.get('https://magento.softwaretestingboard.com/')

    def click_shop_new_yoga(self):
        wait = WebDriverWait(self.driver, 10)
        shop_yoga_btn = self.driver.find_element(By.CLASS_NAME, 'action more button')
        wait.until(ec.visibility_of_element_located(shop_yoga_btn)).click()
