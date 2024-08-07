from selenium.webdriver.chrome import webdriver

from test_ui_evgeny_shit.pages.base_page import BasePage


class SalePage(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
