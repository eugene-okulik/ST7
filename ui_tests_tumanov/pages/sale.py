from ui_tests_tumanov.pages.base_page import Basepage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ui_tests_tumanov.pages.locators import SalePage as loc_sale


class SalPage(Basepage):
    page_url = '/sale.html'

    def check_title(self, text):
        wait = WebDriverWait(self.driver, 2)
        title_card = wait.until(ec.visibility_of_element_located(loc_sale.title_sale))
        assert title_card.text == text

    def check_title_women_page(self, text):
        wait = WebDriverWait(self.driver, 3)
        title_page_women = wait.until(ec.visibility_of_element_located(loc_sale.title_sale))
        assert title_page_women.text == text

    def check_quan_elements(self):
        wait = WebDriverWait(self.driver, 3)
        quan_el = wait.until(ec.visibility_of_element_located(loc_sale.jackets_elements))
        assert quan_el.text == 12



