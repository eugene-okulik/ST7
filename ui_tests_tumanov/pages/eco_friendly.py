from ui_tests_tumanov.pages.base_page import Basepage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ui_tests_tumanov.pages.locators import EcoFriendly as loc


class FriendlyPage(Basepage):
    page_url = '/collections/eco-friendly.html'

    # def card_price(self, text):
    #     wait = WebDriverWait(self.driver, 2)
    #     price = wait.until(ec.visibility_of_element_located(loc.price))
    #     assert price.text == text
    def card_price(self, text):
        found_el = self.find(loc.price)
        assert found_el.text == text

    # def check_price_in_card(self, text):
    #     wait = WebDriverWait(self.driver, 5)
    #     price_card = wait.until(ec.visibility_of_element_located(loc.price))
    #     assert price_card.text == text
    def check_price_in_card(self, text):
        found_el = self.find(loc.price)
        assert found_el.text == text

    # def check_title_in_card(self, text):
    #     wait = WebDriverWait(self.driver, 3)
    #     title_card = wait.until(ec.visibility_of_element_located(loc.card_title))
    #     assert title_card.text == text

    def check_title_in_card(self, text):
        found_el = self.find(loc.card_title)
        assert found_el.text == text
