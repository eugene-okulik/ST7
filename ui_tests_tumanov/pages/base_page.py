import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec


class Basepage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open home pages')
    def open(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Unable to open that pages by url')

    def find(self, locator: tuple):
        wait = WebDriverWait(self.driver, 3)
        return wait.until(
            ec.presence_of_element_located(*locator)
        )

    def find_element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def click_el(self, locator: tuple):
        self.find_element(locator).click()

    def url_new_page(self, url: str):
        return self.driver.current_url == url


