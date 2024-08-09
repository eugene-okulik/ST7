import pytest
from selenium import webdriver
from ui_tests_yevdokiienko.pages.create_nc_account_page import CreateAccountPage
from ui_tests_yevdokiienko.pages.account_page import AccountPage
from ui_tests_yevdokiienko.pages.ef_collection_page import EcoFriendlyCollectionPage
from ui_tests_yevdokiienko.pages.card_page import CartPage
from ui_tests_yevdokiienko.pages.sale_page import SalePage
from ui_tests_yevdokiienko.pages.men_deal_page import MenDealPage
from ui_tests_yevdokiienko.pages.women_deal_page import WomenDealPage
from ui_tests_yevdokiienko.pages.acc_error_page import AccountErrorPage


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
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture()
def ef_collection_page(driver):
    return EcoFriendlyCollectionPage(driver)


@pytest.fixture()
def card_page(driver):
    return CartPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def men_deal_page(driver):
    return MenDealPage(driver)


@pytest.fixture()
def women_deal_page(driver):
    return WomenDealPage(driver)


@pytest.fixture()
def ac_error_page(driver):
    return AccountErrorPage(driver)
