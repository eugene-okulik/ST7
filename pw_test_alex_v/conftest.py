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
    return CreateAccountPage(page)


@pytest.fixture()
def my_account_page(page):
    return Account(page)


@pytest.fixture()
def eco_page(page):
    return EcoPage(page)


@pytest.fixture()
def compare_page(page):
    return ComparePage(page)


@pytest.fixture()
def product_page(page):
    return ProductPage(page)


@pytest.fixture()
def customer_login_page(page):
    return CustomerLoginPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
