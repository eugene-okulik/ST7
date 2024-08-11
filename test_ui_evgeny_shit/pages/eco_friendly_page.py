from test_ui_evgeny_shit.pages.base_page import BasePage
from test_ui_evgeny_shit.locators import EcoFriendlyLocators as eco_loc


class EcoPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def numer_of_items_is(self, count: int) -> bool:
        elements = self.find_elements(eco_loc.cards_li)
        return len(elements) == count
