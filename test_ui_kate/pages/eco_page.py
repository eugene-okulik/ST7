import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import AccountLocators as loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    @allure.step('Checking the Bra element')
    def find_bra(self):
        bra = self.find(loc.BRA)
        self.actions_move_to_element(bra)

    @allure.step('Checking the compared icon')
    def find_compared_icon(self):
        self.find(loc.COMPARE_ICON).click()

    @allure.step('Checking if the item was added to the Compared section')
    def compared_items_added(self):
        self.find(loc.COMPARED_ITEMS).is_displayed
        assert self.find(loc.COMPARED_ITEMS).text == "Electra Bra Top"

    @allure.step('Checking the Tank icon')
    def find_tank(self):
        tank = self.find(loc.TANK)
        self.actions_move_to_element(tank)

    @allure.step('Checking adding to the Wishlist')
    def find_wishlist_icon(self):
        self.find(loc.WISHLIST_ICON).click()

    @allure.step('Checking the pagination in the list view')
    def list_view_element(self):
        self.find(loc.LIST_VIEW_ICON).click()
        assert self.find(loc.LIST_VIEW_PAGINATION).text == '10'
