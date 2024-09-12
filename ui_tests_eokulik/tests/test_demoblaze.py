import pytest


@pytest.mark.smoke
def test_phone_page(home_page, product_page):
    home_page.open()
    home_page.click_product('Sony vaio i7')
    home_page.scroll_page()
    product_page.check_add_to_cart_button(9)


@pytest.mark.e2e
def test_e2e(home_page, product_page, cart_page):
    home_page.open()
    home_page.click_product('Samsung galaxy s6')
    product_page.click_add_to_cart('1')
    product_page.accept_alert()
    cart_page.open()
    cart_page.check_product_in_cart('Samsung galaxy s6')
