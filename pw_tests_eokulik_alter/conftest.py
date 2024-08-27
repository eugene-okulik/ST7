import pytest
from playwright.sync_api import Page, BrowserContext
from pw_tests_eokulik_alter.pages.home_page import HomePage
from pw_tests_eokulik_alter.pages.product_page import ProductPage
from pw_tests_eokulik_alter.pages.cart_page import CartPage


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page


@pytest.fixture()
def home_page(page):
    return HomePage(page)


@pytest.fixture()
def product_page(page):
    return ProductPage(page)


@pytest.fixture()
def cart_page(page):
    return CartPage(page)
