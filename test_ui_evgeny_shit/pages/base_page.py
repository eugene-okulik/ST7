from selenium.webdriver.chrome import webdriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def open(self, url: str) -> None:
        self.driver.get(url)

    def find_element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

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

    def is_correct_number_of_items(self, locator: tuple, count: int) -> bool:
        elements = self.find_elements(locator)
        return len(elements) == count

    def is_equal(self, locator: tuple, text: str) -> bool:
        return self.find_element(locator).text == text

    def is_title_page(self, text: str) -> None:
        return self.driver.title == text
