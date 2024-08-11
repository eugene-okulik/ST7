from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from ui_test_alex_v.pages.base_page import BasePage


class SalePage(BasePage):
    page_url = '/sale.html'

