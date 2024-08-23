import allure
from test_ui_kate.pages.base_page import BasePage
from test_ui_kate.pages.locators import Locators as loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    @allure.step('Checking if the item was added to the Compared section')
    def compared_item_added(self, text):
        self.find(loc.COMPARED_ITEMS).is_displayed
        assert self.find(loc.COMPARED_ITEMS).text == text

    @allure.step('Checking the pagination in the list view')
    def changed_pagination(self, text):
        assert self.find(loc.LIST_VIEW_PAGINATION).text == text
