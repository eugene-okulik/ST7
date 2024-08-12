import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Unable to open that page by url')

    def find(self, locator):
        wait = WebDriverWait(self.driver, 15)
        return wait.until(
            ec.presence_of_element_located(locator)
        )

    def title_page_is(self, text):
        return self.driver.title == text

    def element_visible_is(self, locator):
        return self.find(locator).is_displayed()
