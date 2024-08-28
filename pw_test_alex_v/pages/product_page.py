
from pw_test_alex_v.pages.base_page import BasePage


class ProductPage(BasePage):
    def add_to_compare_product(self):
        add_to_compare = self.page.locator("//div[@class='product-addto-links']/a[2]")
        add_to_compare.click()

    def add_to_wish_list(self):
        add_to_wishlist = self.page.locator("//div[@class='product-addto-links']/a[1]")
        add_to_wishlist.click()

    def go_to_comparison_list(self):
        comparison_list_button = self.page.locator('comparison list').first
        comparison_list_button.click()

    def get_product_title(self):
        product_title = self.page.locator("//span[@class='base']").inner_text()
        return product_title
