import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Opening the page')
    def open(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Unable to open that page by url')

    @allure.step('Finding an element')
    def find(self, locator: tuple):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.presence_of_element_located(locator))

    @allure.step('Sending keys to an element')
    def actions_send_keys(self, key_value):
        actions = ActionChains(self.driver)
        return actions.send_keys(key_value).perform()

    @allure.step('Moving to an element')
    def actions_move_to_element(self, item):
        actions = ActionChains(self.driver)
        return actions.move_to_element(item).perform()

    @allure.step('Scrolling the page')
    def scroll_page(self, pixels=None, start=0):
        if pixels:
            self.driver.execute_script(f"window.scrollTo({start}, {pixels})")
        else:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")