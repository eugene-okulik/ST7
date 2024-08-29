from playwright.sync_api import expect

from pw_tests_evgeny_shit.pages.base_page import BasePage
from pw_tests_evgeny_shit.locators import SaleLocators as sale_loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def click_on_man_sale_card(self):
        self.click_element(sale_loc.card_man_sale)

    def is_men_sale_title_visible(self):
        return self.is_element_visible(sale_loc.men_sale_title)

    def is_title_luma_gear_steal_visible(self):
        return self.is_element_visible(sale_loc.luma_gear_steal)

    def title_page_is_(self, text: str) -> bool:
        expect(self.page).to_have_title(text)
        return True

    def is_element_visible(self, selector: str) -> bool:
        expect(self.page.locator(selector)).to_be_visible()
        return True
