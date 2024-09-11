import pytest
from playwright.sync_api import Page, BrowserContext
from pw_tests_kate.pages.account_page import AccountPage
from pw_tests_kate.pages.customer_account_page import CustomerAccountPage
from pw_tests_kate.pages.eco_page import EcoFriendlyPage
from pw_tests_kate.pages.not_logged_in import NotLoggedIn
from pw_tests_kate.pages.sale_page import SalePage
from pw_tests_kate.pages.gear_page import GearPage
from pw_tests_kate.pages.women_page import WomenPage


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page


@pytest.fixture()
def account_page(page: Page) -> AccountPage:
    return AccountPage(page)


@pytest.fixture()
def customer_account(page: Page) -> CustomerAccountPage:
    return CustomerAccountPage(page)


@pytest.fixture()
def eco_friendly(page):
    return EcoFriendlyPage(page)


@pytest.fixture()
def not_logged_in(page):
    return NotLoggedIn(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def gear_page(page):
    return GearPage(page)


@pytest.fixture()
def women_page(page):
    return WomenPage(page)
