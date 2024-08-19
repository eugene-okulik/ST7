from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
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

    def find_element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def wait_for_element_visible(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        """Wait for an element specified by the locator to be visible"""
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def find_elements(self, locator: tuple) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def click_element(self, locator: tuple) -> None:
        self.find_element(locator).click()

    def send_keys(self, locator: tuple, text: str) -> None:
        self.find_element(locator).send_keys(text)

    def is_current_url(self, url: str) -> bool:
        return self.driver.current_url == url

    def is_element_visible(self, locator: tuple) -> bool:
        return self.find_element(locator).is_displayed()

    def is_equal(self, locator: tuple, text: str) -> bool:
        return text in self.find_element(locator).text

    def is_title_page(self, text: str) -> bool:
        return self.driver.title == text
