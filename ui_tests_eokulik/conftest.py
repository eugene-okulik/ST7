import pytest
from selenium import webdriver
from ui_tests_eokulik.pages.home_page import HomePage
from ui_tests_eokulik.pages.product_page import ProductPage
from ui_tests_eokulik.pages.cart_page import CartPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)
