from pw_tests_tuman.pages.base_page import Basepage
from playwright.sync_api import expect, Locator
from pw_tests_tuman.pages.locators import SalePage as loc_sale


class SalPage(Basepage):
    page_url = '/sale.html'

    def check_title(self, text):
        title_card = self.find(loc_sale.title_sale)
        expect(title_card).to_have_text(text)

    def check_title_women_page(self, text):
        title_page_women = self.find(loc_sale.title_women_page)
        expect(title_page_women).to_have_text(text, timeout=10000)

    def click_button_shop(self):
        self.click_el(loc_sale.button_shop)
