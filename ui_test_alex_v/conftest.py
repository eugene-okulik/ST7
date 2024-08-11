import pytest
from selenium import webdriver
from ui_test_alex_v.pages.create_account_page import CreateAccountPage
from ui_test_alex_v.pages.account_page import Account


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
def my_account_page(driver):
    return Account(driver)

