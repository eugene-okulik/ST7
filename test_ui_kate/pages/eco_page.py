import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import Locators as loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    @allure.step('Find and click Bra element and add it to compared items')
    def add_bra_item_to_compare(self):
        self.scroll_page(500)
        self.find_and_hover_element(loc.BRA_ITEM)
        self.find_and_click_element(loc.COMPARE_ICON)

    @allure.step('Checking if the item was added to the Compared section')
    def check_bra_added(self, text):
        self.find_element(loc.COMPARED_ITEMS).is_displayed
        assert self.find_element(loc.COMPARED_ITEMS).text == text

    @allure.step('Find and click Tank element and add try to add it to Wishlist')
    def add_tank_item_to_wishlist(self):
        self.scroll_page(500)
        self.find_and_hover_element(loc.TANK_ITEM)
        self.find_and_click_element(loc.WISHLIST_ICON)

    @allure.step('Changing how the items are displayed on the page')
    def change_the_items_view_to_be_list(self):
        self.find_and_click_element(loc.LIST_VIEW_ICON)

    @allure.step('Checking the pagination in the list view')
    def check_the_pagination_changed_to_be_10(self):
        assert self.find_element(loc.LIST_VIEW_PAGINATION).text == '10'
