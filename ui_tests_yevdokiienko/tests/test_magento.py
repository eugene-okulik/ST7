import allure


@allure.feature('Registration page')
@allure.tag('Positive opened registration page')
def test_form_is_able(create_account_page):
    create_account_page.open()
    create_account_page.check_form_is_able('Create New Customer Account')


@allure.feature('Registration page')
@allure.tag('Positive registration')
def test_create_new_customer_form(create_account_page, account_page):
    create_account_page.open()
    create_account_page.fill_first_name('eduard')
    create_account_page.fill_last_name('y')
    create_account_page.fill_email('edddd@gmail.com')
    create_account_page.fill_password('EDU1111edu')
    create_account_page.fill_confirm_password('EDU1111edu')
    create_account_page.click_create()
    account_page.check_registration_success('Thank you for registering with Main Website Store.')


@allure.feature('Registration page')
@allure.tag('Negative registration with wrong conformation password')
def test_wrong_confirm_password(create_account_page):
    create_account_page.open()
    create_account_page.fill_first_name('eduard')
    create_account_page.fill_last_name('y')
    create_account_page.fill_email('eddd@gmail.com')
    create_account_page.fill_password('EDU1111edu')
    create_account_page.fill_confirm_password('e')
    create_account_page.click_create()
    create_account_page.password_confirmation_error('Please enter the same value again.')


@allure.feature('Eco-friendly products page')
@allure.tag('Positive choose product')
def test_choose_product(ef_collection_page, card_page):
    ef_collection_page.open()
    ef_collection_page.click_product('1')
    card_page.check_product_in_cart('Ana Running Short')


@allure.feature('Eco-friendly products page')
@allure.tag('Positive add to compare list')
def test_add_to_compare(ef_collection_page):
    ef_collection_page.open()
    ef_collection_page.scroll_page(300)
    ef_collection_page.add_to_compare('1')
    ef_collection_page.scroll_page()
    ef_collection_page.check_compare_products('Ana Running Short')


@allure.feature('Eco-friendly products page')
@allure.tag('Negative add to wish list')
def test_add_to_wish_list(ef_collection_page, ac_error_page):
    ef_collection_page.open()
    ef_collection_page.scroll_page(400)
    ef_collection_page.add_to_wish_list('1')
    ac_error_page.add_to_wish_list_failed('You must login or register to add items to your wishlist.')


@allure.feature('Sale page')
@allure.tag('Positive open sale page')
def test_open_sale_page(sale_page):
    sale_page.open()
    sale_page.check_sale_page_able('Sale')


@allure.feature('Sale page')
@allure.tag('Positive verify sale')
def test_check_sale(sale_page):
    sale_page.open()
    sale_page.scroll_page()
    sale_page.verify_percent_of_sale('20')


@allure.feature('Sale page')
@allure.tag('Positive open choose men deals')
def test_men_deals_able(sale_page, men_deal_page):
    sale_page.open()
    sale_page.scroll_page(500)
    sale_page.click_men_deals()
    men_deal_page.check_men_page_opened('Men Sale')


@allure.feature('Sale page')
@allure.tag('Positive open choose women deals')
def test_women_deals_able(sale_page, women_deal_page):
    sale_page.open()
    sale_page.scroll_page(200)
    sale_page.click_women_deals()
    women_deal_page.check_women_page_opened('Women Sale')
