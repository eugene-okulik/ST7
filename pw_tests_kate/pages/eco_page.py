import allure
from pw_tests_kate.pages.base_page import BasePage
from pw_tests_kate.pages.locators import Locators as loc
from playwright.sync_api import expect


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    @allure.step('Find and click Bra element and add it to compared items')
    def add_bra_item_to_compare(self):
        self.move_to_element(loc.BRA_ITEM)
        self.find_and_click_element(loc.COMPARE_ICON)

    @allure.step('Checking if the item was added to the Compared section')
    def check_bra_added(self, text):
        self.page.wait_for_selector(loc.COMPARED_ITEMS, timeout=30000)
        expect(self.find_element_by_locator(loc.COMPARED_ITEMS)).to_have_text(text)

    @allure.step('Changing how the items are displayed on the page')
    def change_the_items_view_to_be_list(self):
        self.find_element_by_locator(loc.LIST_VIEW_ICON).first.click()

    @allure.step('Checking the pagination in the list view')
    def check_the_pagination_changed_to_be_(self, number):
        expect(self.find_element_by_locator(loc.LIST_VIEW_PAGINATION)).to_have_text(number)

    @allure.step('Find and click Tank element and add try to add it to Wishlist')
    def add_tank_item_to_wishlist(self):
        self.move_to_element(loc.TANK_ITEM)
        self.find_and_click_element(loc.WISHLIST_ICON)
