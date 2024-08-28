from playwright.sync_api import expect
from pw_test_alex_v.pages.base_page import BasePage


class ComparePage(BasePage):

    def compared_product_title_displayed_is(self, test_product_title):
        prodict_title = self.page.locator('product-item-name').inner_text()
        expect(prodict_title).to_equal(test_product_title)
