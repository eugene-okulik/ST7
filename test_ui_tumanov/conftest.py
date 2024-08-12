import pytest
from selenium import webdriver
from test_ui_tumanov.pages.create_new_account import InputPage
from test_ui_tumanov.pages.customer_account import Customer
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # driver.quit()


@pytest.fixture()
def create_account(driver):
    return InputPage(driver)


@pytest.fixture()
def check_fio_email(driver):
    return Customer(driver)


# def test_probnik(driver):
#     driver.get('https://magento.softwaretestingboard.com/customer/account/')
#     validatia = driver.find_element(By.XPATH, '//div[@class="box-content"]/p').text
#     list_item = ['Vitek', 'Tuman', 'test@bk.com']
#     for el in list_item:
#         assert el in validatia