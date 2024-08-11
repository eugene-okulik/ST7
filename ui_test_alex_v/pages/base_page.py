import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open home page')
    def open(self):
        if self.page_url:
            self.driver.get('https://magento.softwaretestingboard.com/customer/account/')
        else:
            raise NotImplementedError('Unable to open that page by url')

    def find(self, locator: tuple):
        # return self.driver.find_element(*locator)
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            ec.presence_of_element_located(locator)
        )
