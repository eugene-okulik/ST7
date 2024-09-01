from pw_test_alex_v.pages.base_page import BasePage


class SalePage(BasePage):
    page_url = '/sale.html'

    def get_section_titles(self):
        self.page.wait_for_selector("//ul[@class='items']//li/a")
        sections = self.page.query_selector_all("//ul[@class='items']//li/a")
        section_titles = [section.text_content() for section in sections]
        print(f"Found sections: {section_titles}")
        return section_titles

    def get_discount_value(self):
        discount_element = self.page.wait_for_selector(".block-promo.sale-20-off")
        discount_value = discount_element.text_content()
        print(discount_value)
        return discount_value
