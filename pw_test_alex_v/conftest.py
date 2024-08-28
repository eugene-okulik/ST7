import pytest
from playwright.sync_api import Page, BrowserContext
from pw_test_alex_v.pages.compare_page import ComparePage
from pw_test_alex_v.pages.create_account_page import CreateAccountPage
from pw_test_alex_v.pages.account_page import Account
from pw_test_alex_v.pages.customer_login import CustomerLoginPage
from pw_test_alex_v.pages.eco_page import EcoPage
from pw_test_alex_v.pages.product_page import ProductPage
from pw_test_alex_v.pages.sale_page import SalePage


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page


@pytest.fixture()
def create_account_page(page):
    return CreateAccountPage(driver)


@pytest.fixture()
def my_account_page(page):
    return Account(driver)


@pytest.fixture()
def eco_page(page):
    return EcoPage(driver)


@pytest.fixture()
def compare_page(page):
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
