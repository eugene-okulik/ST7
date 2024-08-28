import pytest
from playwright.sync_api import Page, BrowserContext
from pw_test_ui_dmitrii.pages.create_new_customer_account import NewCustomerAccount
from pw_test_ui_dmitrii.pages.eco_friendly_supplies import EcoProducts
from pw_test_ui_dmitrii.pages.my_account import MyAccountPage
from pw_test_ui_dmitrii.pages.product_page import ProductPage
from pw_test_ui_dmitrii.pages.login_page import LoginPage
from pw_test_ui_dmitrii.pages.sales_page import Sales
from pw_test_ui_dmitrii.pages.deals_page import DealsPage


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page


@pytest.fixture()
def create_account_page(page):
    return NewCustomerAccount(page)


@pytest.fixture()
def eco_products_page(page):
    return EcoProducts(page)


@pytest.fixture()
def my_account_page(page):
    return MyAccountPage(page)


@pytest.fixture()
def product_page(page):
    return ProductPage(page)


@pytest.fixture()
def login_page(page):
    return LoginPage(page)


@pytest.fixture()
def sales_page(page):
    return Sales(page)


@pytest.fixture()
def deals_page(page):
    return DealsPage(page)
