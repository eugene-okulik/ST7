from test_ui_kate.pages.locators import Locators as loc


def test_password_field(account_page):
    account_page.open_page()
    account_page.find_and_click_element(loc.PASSWORD_FIELD)
    account_page.send_keys_to_element('Barsuki')
    account_page.password_strength('Weak')


def test_email_field(account_page):
    account_page.open_page()
    account_page.find_and_click_element(loc.EMAIL_FIELD)
    account_page.send_keys_to_element('skdfjg.com')
    account_page.find_and_click_element(loc.CREATE_BUTTON)
    account_page.invalid_email_error('Please enter a valid email address (Ex: johndoe@domain.com).')


def test_registration(account_page, success_account):
    account_page.open_page()
    account_page.find_and_click_element(loc.FIRST_NAME_FIELD)
    account_page.send_keys_to_element('Kate')
    account_page.find_and_click_element(loc.LAST_NAME_FIELD)
    account_page.send_keys_to_element('Test')
    account_page.find_and_click_element(loc.EMAIL_FIELD)
    account_page.send_keys_to_element('katetestY@yahoo.com')
    account_page.find_and_click_element(loc.PASSWORD_FIELD)
    account_page.send_keys_to_element('Barsuki07')
    account_page.find_and_click_element(loc.CONFIRM_PASSWORD_FIELD)
    account_page.send_keys_to_element('Barsuki07')
    account_page.find_and_click_element(loc.CREATE_BUTTON)
    success_account.find_element(loc.SUCCESS_CONFIRMATION)
    success_account.success_registration('Thank you for registering with Main Website Store.')


def test_to_compare_item(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.scroll_page(500)
    eco_friendly.find_and_hover_element(loc.BRA_ITEM)
    eco_friendly.find_and_click(loc.COMPARE_ICON)
    eco_friendly.compared_item_added('Electra Bra Top')


def test_to_wishlist_item(eco_friendly, not_logged_in):
    eco_friendly.open_page()
    eco_friendly.scroll_page(500)
    eco_friendly.find_and_hover_element(loc.TANK_ITEM)
    eco_friendly.find_and_click(loc.WISHLIST_ICON)
    not_logged_in.erro_without_login(loc.ERROR_MESSAGE)


def test_page_list_view(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.find_and_click(loc.LIST_VIEW_ICON)
    eco_friendly.changed_pagination('10')


def test_sale_redirect_to_gear_page(sale_page, gear_page):
    sale_page.open_page()
    sale_page.find_and_click_element(loc.LUMA_GEAR_LINK)
    gear_page.check_correct_redirect('Gear')


def test_sale_add_to_cart(sale_page, gear_page):
    sale_page.open_page()
    sale_page.find_and_click_element(loc.LUMA_GEAR_LINK)
    gear_page.find_and_hover_element(loc.BOTTLE_ICON)
    gear_page.find_and_click(loc.ADD_TO_CART_ICON)
    gear_page.check_number_items_in_cart('1')


def test_sale_redirect_to_proper_page(sale_page, women_page):
    sale_page.open_page()
    sale_page.find_and_click_element(loc.BRAS_AND_TANKS_LINK)
    women_page.check_page_title('Bras & Tanks')
