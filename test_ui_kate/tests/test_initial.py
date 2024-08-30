def test_password_field(account_page):
    account_page.open_page()
    account_page.type_password('Barsuki')
    account_page.check_password_strength(text='Weak')


def test_email_field(account_page):
    account_page.open_page()
    account_page.enter_email_address('skdfjg.com')
    account_page.click_create_account_button()
    account_page.check_invalid_email_error(text='Please enter a valid email address (Ex: johndoe@domain.com).')


def test_registration(account_page, success_account):
    account_page.open_page()
    account_page.enter_first_name('Kate')
    account_page.enter_last_name('TestOne')
    account_page.enter_email_address('katetestABC@yahoo.com')
    account_page.type_password('Barsuki07!')
    account_page.confirm_password('Barsuki07!')
    account_page.click_create_account_button()
    success_account.confirm_successful_registration(text='Thank you for registering with Main Website Store.')


def test_to_compare_item(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.add_bra_item_to_compare()
    eco_friendly.check_bra_added('Electra Bra Top')


def test_to_wishlist_item(eco_friendly, not_logged_in):
    eco_friendly.open_page()
    eco_friendly.add_tank_item_to_wishlist()
    not_logged_in.check_item_not_added_without_logging_in()


def test_page_list_view(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.change_the_items_view_to_be_list()
    eco_friendly.check_the_pagination_changed_to_be_('10')


def test_sale_page_redirects_to_gear_page(sale_page, gear_page):
    sale_page.open_page()
    sale_page.click_luma_gear_link()
    gear_page.check_page_title('Gear')


def test_add_to_cart(sale_page, gear_page):
    sale_page.open_page()
    sale_page.click_luma_gear_link()
    gear_page.add_bottle_to_cart()
    gear_page.check_number_items_in_cart('1')


def test_sale_page_redirects_to_bras_and_tanks_page(sale_page, women_page):
    sale_page.open_page()
    sale_page.click_bras_and_tanks_link()
    women_page.check_page_title('Bras & Tanks')
