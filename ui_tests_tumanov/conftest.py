import pytest
from selenium import webdriver
from ui_tests_tumanov.pages.create_new_account import CreateAccountPage
from ui_tests_tumanov.pages.eco_friendly import FriendlyPage
from ui_tests_tumanov.pages.sale import SalPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # driver.quit()


@pytest.fixture()
def create_account(driver):
    return CreateAccountPage(driver)


@pytest.fixture()
def eco_friendly(driver):
    return FriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalPage(driver)
