import pytest
from selenium import webdriver

from ui_test_alex_v.pages.home_page import HomePage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)
