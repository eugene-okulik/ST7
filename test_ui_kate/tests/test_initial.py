from test_ui_kate.pages.locators import AccountLocators as loc


def test_password_field(account_page):
    account_page.open()
    account_page.find_field(loc.PASSWORD_INPUT)
    account_page.send_keys('Barsuki')
    account_page.weak_password()


def test_email_field(account_page):
    account_page.open()
    account_page.find_field(loc.EMAIL_INPUT)
    account_page.send_keys('skdfjg.com')
    account_page.find_field(loc.CREATE_BUTTON)
    account_page.invalid_email()
    

def test_registration(account_page, success_account):
    account_page.open()
    account_page.find_field(loc.FIRST_NAME)
    account_page.send_keys('Kate')
    account_page.find_field(loc.LAST_NAME)
    account_page.send_keys('Test')
    account_page.find_field(loc.EMAIL_INPUT)
    account_page.send_keys('katetestX@yahoo.com')
    account_page.find_field(loc.PASSWORD_INPUT)
    account_page.send_keys('Barsuki07')
    account_page.find_field(loc.CONFIRM_PASSWORD)
    account_page.send_keys('Barsuki07')
    account_page.find_field(loc.CREATE_BUTTON)
    success_account.find(loc.SUCCESS_CONFIRMATION)
    success_account.success_confirmation()


def test_compare(eco_friendly):
    eco_friendly.open()
    eco_friendly.scroll_page(500)
    eco_friendly.find_bra()
    eco_friendly.find_compared_icon()
    eco_friendly.compared_items_added()


def test_wishlist(eco_friendly, not_logged_in):
    eco_friendly.open()
    eco_friendly.scroll_page(600)
    eco_friendly.find_tank()
    eco_friendly.find_wishlist_icon()
    not_logged_in.find_error_alert()


def test_list_view(eco_friendly):
    eco_friendly.open()
    eco_friendly.list_view_element()


def test_sale_gear_page(sale_page, gear_page):
    sale_page.open()
    sale_page.gear_page()
    gear_page.correct_redirect()


def test_sale_cart(sale_page, gear_page):
    sale_page.open()
    sale_page.gear_page()
    gear_page.bottle_icon()
    gear_page.add_to_cart()
    gear_page.check_cart_number()


def test_sale_redirect(sale_page, women_page):
    sale_page.open()
    sale_page.bras_and_tops()
    women_page.page_title()
