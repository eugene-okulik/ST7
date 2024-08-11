import pytest
from selenium import webdriver
from ui_test_alex_v.pages.create_account_page import CreateAccountPage
from ui_test_alex_v.pages.my_account_page import MyAccount


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()




@pytest.fixture()
def create_account_page(driver):
    return CreateAccountPage(driver)


@pytest.fixture()
def my_account_page(driver):
    return MyAccount(driver)
