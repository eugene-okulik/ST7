import allure
from selenium.webdriver.common.by import By
from test_ui_tumanov.pages.base_page import Basepage
import pytest


class InputPage(Basepage):
    # page_url = 'customer/account/create/'

    @allure.step('Open page form')
    def open(self):
        self.driver.get(f'https://magento.softwaretestingboard.com/customer/account/create/')

    def input_met(self, loc, send_text):
        self.driver.find_element(*loc).send_keys(send_text)

    def click_button(self, loc):
        self.driver.find_element(*loc).click()

    # def check_probnikk(self):
    #     validatia = driver.find_element(By.XPATH, '//div[@class="box-content"]/p').text
    #     list_item = ['Vitek', 'Tuman', 'test@bk.com']
    #     for el in list_item:
    #         assert el in validatia
