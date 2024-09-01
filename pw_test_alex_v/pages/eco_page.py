from playwright.sync_api import Page, expect
import allure
import random

from pw_test_alex_v.pages.base_page import BasePage


class EcoPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    @allure.step('Sort products by name')
    def sort_products_by_name(self) -> bool:
        sort_dropdown = self.page.locator("select#sorter").first
        sort_dropdown.wait_for(state="visible", timeout=10000)
        sort_dropdown.click()

        sort_by_name_option = self.find("//option[@value='name']").first
        sort_by_name_option.wait_for(state="visible", timeout=10000)
        sort_by_name_option.click()

        expect(self.page.locator("select#sorter option[selected='selected']")).to_have_text("Product Name")

        product_names = self.page.locator(".product-item-name a").all_inner_texts()
        names = [name.strip() for name in product_names]

        return names == sorted(names)

    @allure.step('Click on a product')
    def choose_product(self):
        product_elements = self.page.locator("//a[@class='product-item-link']").first
        product_elements.wait_for(state="visible", timeout=10000)

        all_products = product_elements.all()

        if not all_products:
            raise Exception("No products found on the page")

        random_product = random.choice(all_products)
        random_product.click()
