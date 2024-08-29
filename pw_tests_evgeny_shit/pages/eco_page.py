from pw_tests_evgeny_shit.pages.base_page import BasePage
from pw_tests_evgeny_shit.locators import EcoFriendlyLocators as eco_loc


class EcoPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def click_on_card_bella_tank(self):
        self.click_element(eco_loc.cards_li_4)

    def visible_card_title_is_(self, title: str) -> bool:
        return self.is_equal(eco_loc.cards_4_title, title)

    def number_of_cards_on_page_is_(self, count: int) -> bool:
        elements = self.find_elements(eco_loc.cards_li)
        return len(elements) == count

    def product_daria_bikram_pant_price_is_(self, expected_price: str) -> bool:
        return self.is_equal(eco_loc.span_card, expected_price)
