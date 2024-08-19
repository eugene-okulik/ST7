import pytest
from selenium import webdriver
from test_ui_kate.pages.account_page import AccountPage
from test_ui_kate.pages.customer_account_page import CustomerAccountPage
from test_ui_kate.pages.eco_page import EcoFriendlyPage
from test_ui_kate.pages.not_logged_in_page import NotLoggedIn
from test_ui_kate.pages.sale_page import SalePage
from test_ui_kate.pages.gear_page import GearPage
from test_ui_kate.pages.women_page import WomenPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture()
def success_account(driver):
    return CustomerAccountPage(driver)


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def not_logged_in(driver):
    return NotLoggedIn(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def gear_page(driver):
    return GearPage(driver)


@pytest.fixture()
def women_page(driver):
    return WomenPage(driver)
