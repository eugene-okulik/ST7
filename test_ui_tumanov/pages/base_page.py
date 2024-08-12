import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Basepage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open home page')
    def open(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Unable to open that page by url')

    def find(self, locator: tuple):
        # return self.driver.find_element(*locator)
        wait = WebDriverWait(self.driver, 3)
        return wait.until(
            ec.presence_of_element_located(locator)
        )
