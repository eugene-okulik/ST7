from pw_tests_tuman.pages.base_page import Basepage
from playwright.sync_api import expect
from pw_tests_tuman.pages.locators import EcoFriendly as loc


class FriendlyPage(Basepage):
    page_url = '/collections/eco-friendly.html'

    def card_price(self, text):
        found_el = self.find(loc.price)
        expect(found_el).to_have_text(text)
        # assert found_el.text == text

    def click_card_number(self):
        self.click_el(loc.cards_number)

    def check_title_in_card(self, text):
        found_el = self.find(loc.card_title)
        expect(found_el).to_have_text(text)
        # assert found_el.text == text
