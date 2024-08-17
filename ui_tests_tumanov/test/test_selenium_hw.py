from ui_tests_tumanov.pages.locators import (CreateAccount as loc,
                                             EcoFriendly as eco,
                                             SalePage as sal)


def test_create_account(create_account):
    create_account.open()
    create_account.input_met(loc.first_name_loc, "Viteenq")
    create_account.input_met(loc.last_name_loc, "Tumaanq")
    create_account.input_met(loc.email_loc, 'tsttnqhr@bk.com')
    create_account.input_met(loc.password_loc, '923456zZz#!!')
    create_account.input_met(loc.password_confirmation_loc, '923456zZz#!!')
    create_account.click_el(loc.click_button_account)
    create_account.check_text_is('Thank you for registering with Main Website Store.')


def test_check_re_registration(create_account):
    create_account.open()
    create_account.input_met(loc.first_name_loc, "Viteenq")
    create_account.input_met(loc.last_name_loc, "Tumaanq")
    create_account.input_met(loc.email_loc, 'tsttnq@bk.com')
    create_account.input_met(loc.password_loc, '923456zZz#!!')
    create_account.input_met(loc.password_confirmation_loc, '923456zZz#!!')
    create_account.click_el(loc.click_button_account)
    create_account.check_text_is('There is already an'
                                 ' account with this email address. If you are sure that it is your'
                                 ' email address, click here to get your password and access your'
                                 ' account.')


def test_check_message_text_input(create_account):
    create_account.open()
    create_account.input_met(loc.first_name_loc, "")
    create_account.click_el(loc.click_button_account)


def test_price_in_card(eco_friendly):
    eco_friendly.open()
    eco_friendly.card_price('$40.00')


def test_eco_card_click(eco_friendly):
    eco_friendly.open()
    eco_friendly.click_el(eco.cards_number)
    eco_friendly.check_price_in_card('$40.00')


def test_title_in_card(eco_friendly):
    eco_friendly.open()
    eco_friendly.click_el(eco.cards_number)
    eco_friendly.check_title_in_card('Ana Running Short')


def test_title_sale(sale_page):
    sale_page.open()
    # sale_page.check_title('Sale')
    sale_page.find(sal.title_sale)


def test_title_women_page(sale_page):
    sale_page.open()
    sale_page.click_el(sal.button_shop)
    sale_page.check_title_women_page('Women Sale')


def test_quantity_el(sale_page):
    sale_page.open()
    sale_page.click_el(sal.jackets)
    sale_page.check_quan_elements()
