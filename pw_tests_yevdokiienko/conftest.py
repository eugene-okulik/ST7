import pytest
from playwright.sync_api import Page, BrowserContext
from pw_tests_yevdokiienko.pages.create_nc_account_page import CreateAccountPage
from pw_tests_yevdokiienko.pages.account_page import AccountPage
from pw_tests_yevdokiienko.pages.ef_collection_page import EcoFriendlyCollectionPage
from pw_tests_yevdokiienko.pages.card_page import CartPage
from pw_tests_yevdokiienko.pages.sale_page import SalePage
from pw_tests_yevdokiienko.pages.men_deal_page import MenDealPage
from pw_tests_yevdokiienko.pages.women_deal_page import WomenDealPage
from pw_tests_yevdokiienko.pages.acc_error_page import AccountErrorPage


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page


@pytest.fixture()
def create_account_page(page):
    return CreateAccountPage(page)


@pytest.fixture()
def account_page(page):
    return AccountPage(page)


@pytest.fixture()
def ef_collection_page(page):
    return EcoFriendlyCollectionPage(page)


@pytest.fixture()
def card_page(page):
    return CartPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def men_deal_page(page):
    return MenDealPage(page)


@pytest.fixture()
def women_deal_page(page):
    return WomenDealPage(page)


@pytest.fixture()
def ac_error_page(page):
    return AccountErrorPage(page)
