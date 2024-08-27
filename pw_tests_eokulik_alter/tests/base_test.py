from pw_tests_eokulik_alter.pages.home_page import HomePage
from pw_tests_eokulik_alter.pages.product_page import ProductPage
from pw_tests_eokulik_alter.pages.cart_page import CartPage
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import BrowserContext
import random


class BaseTest:
    home_page: HomePage
    product_page: ProductPage
    cart_page: CartPage
    LALALA: str
    constant_id = None

    @pytest.fixture(autouse=True)
    def setup(self, request: SubRequest, context: BrowserContext):
        page = context.new_page()
        request.cls.page = page
        request.cls.LALALA = 'HAHAHA'

        request.cls.home_page = HomePage(page)
        request.cls.product_page = ProductPage(page)
        request.cls.cart_page = CartPage(page)

    @staticmethod
    def generate_constant():
        return random.randrange(100, 100000)

    # def setup_method(self):
    #     self.home_page = HomePage(self.page)
    #     self.product_page = ProductPage(self.page)
    #     self.cart_page = CartPage(self.page)
