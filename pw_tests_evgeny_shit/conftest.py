import pytest
from playwright.sync_api import Page, BrowserContext

from pw_tests_evgeny_shit.pages.acc_page import AccountPage
from pw_tests_evgeny_shit.pages.eco_page import EcoPage
from pw_tests_evgeny_shit.pages.sale_page import SalePage


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page


@pytest.fixture
def create_account_page(page: Page) -> AccountPage:
    return AccountPage(page)


@pytest.fixture
def eco_friendly_page(page: Page) -> EcoPage:
    return EcoPage(page)


@pytest.fixture
def sale_page(page: Page) -> SalePage:
    return SalePage(page)
