from selenium.webdriver.common.by import By
from test_ui_tumanov.pages.base_page import Basepage


class Customer(Basepage):
    page_url = 'https://magento.softwaretestingboard.com/customer/account/'

    def customer_account(self):
        validatia = self.driver.find_element(By.XPATH, '//div[@class="box-content"]/p').text
        list_item = ['Vite', 'Tuma', 'testt@bk.com']
        for el in list_item:
            assert el in validatia
