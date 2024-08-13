import pytest
from selenium import webdriver

from ui_test_alex_v.pages.compare_page import ComparePage
from ui_test_alex_v.pages.create_account_page import CreateAccountPage
from ui_test_alex_v.pages.account_page import Account
from ui_test_alex_v.pages.customer_login import CustomerLoginPage
from ui_test_alex_v.pages.eco_page import EcoPage
from ui_test_alex_v.pages.product_page import ProductPage
from ui_test_alex_v.pages.sale_page import SalePage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def create_account_page(driver):
    return CreateAccountPage(driver)


@pytest.fixture()
def my_account_page(driver):
    return Account(driver)


@pytest.fixture()
def eco_page(driver):
    return EcoPage(driver)


@pytest.fixture()
def compare_page(driver):
    return ComparePage(driver)


@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture()
def customer_login_page(driver):
    return CustomerLoginPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
