import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from test_ui_evgeny_shit.pages.create_account_page import AccountPage
from test_ui_evgeny_shit.pages.eco_friendly_page import EcoPage
from test_ui_evgeny_shit.pages.sale_page import SalePage


@pytest.fixture
def driver(request) -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver: webdriver.Chrome = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def create_account_page(driver: WebDriver) -> AccountPage:
    return AccountPage(driver)


@pytest.fixture
def eco_friendly_page(driver: WebDriver) -> EcoPage:
    return EcoPage(driver)


@pytest.fixture
def sale_page(driver: WebDriver) -> SalePage:
    return SalePage(driver)