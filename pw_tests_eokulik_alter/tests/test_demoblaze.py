from pw_tests_eokulik_alter.tests.base_test import BaseTest


class TestDemoblaze(BaseTest):

    def test_phone_page(self):
        self.home_page.open()
        self.home_page.click_product('Sony vaio i7')
        self.home_page.scroll_page()
        self.product_page.check_add_to_cart_button(9)
        print(self.LALALA)
        print(self.constant_id)

    def test_e2e(self):
        self.home_page.open()
        self.home_page.click_product('Samsung galaxy s6')
        self.product_page.click_add_to_cart('1')
        self.product_page.accept_alert()
        self.cart_page.open()
        self.cart_page.check_product_in_cart('Samsung galaxy s6')
        print(self.constant_id)
