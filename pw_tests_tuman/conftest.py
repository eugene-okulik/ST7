import pytest
from playwright.sync_api import Page, BrowserContext
from pw_tests_tuman.pages.create_new_account import CreateAccountPage
from pw_tests_tuman.pages.eco_friendly import FriendlyPage
from pw_tests_tuman.pages.sale import SalPage


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page


@pytest.fixture()
def create_account(page: Page) -> CreateAccountPage:
    return CreateAccountPage(page)


@pytest.fixture()
def eco_friendly(page: Page) -> FriendlyPage:
    return FriendlyPage(page)


@pytest.fixture()
def sale_page(page: Page) -> SalPage:
    return SalPage(page)
