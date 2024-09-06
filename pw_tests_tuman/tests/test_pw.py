from pw_tests_tuman.pages.locators import (CreateAccount as loc, SalePage as sal)


def test_create_account(create_account):
    create_account.open()
    create_account.filling_out_the_form('Viteenq', "Tumaanq",
                                        'tsalttr@bk.com', '923456zZz#!!',
                                        '923456zZz#!!')
    create_account.click_button_create()
    create_account.wait_for_element_visible(loc.thank_message)
    create_account.check_text_is('Thank you for registering with Main Website Store.')


def test_check_re_registration(create_account):
    create_account.open()
    create_account.filling_out_the_form('Viteenq', "Tumaanq",
                                        'tsalttr@bk.com', '923456zZz#!!',
                                        '923456zZz#!!')
    create_account.click_button_create()
    create_account.wait_for_element_visible(loc.error_message)  # Не пойму как убрать локатор
    create_account.check_text_is('There is already an'
                                 ' account with this email address. If you are sure that it is your'
                                 ' email address, click here to get your password and access your'
                                 ' account.')


def test_check_message_text_input(create_account):
    create_account.open()
    create_account.check_empty_input_message('This is a required field.')
# Помочь


def test_price_in_card(eco_friendly):
    eco_friendly.open()
    eco_friendly.card_price('$40.00')


def test_eco_card_click(eco_friendly):
    eco_friendly.open()
    eco_friendly.click_card_number()
    eco_friendly.card_price('$40.00')


def test_title_in_card(eco_friendly):
    eco_friendly.open()
    eco_friendly.click_card_number()
    eco_friendly.check_title_in_card('Ana Running Short')


def test_title_sale(sale_page):
    sale_page.open()
    sale_page.check_title('Sale')


def test_title_women_page(sale_page):
    sale_page.open()
    sale_page.click_button_shop()
    # sale_page.wait_for_element_visible(sal.title_women_page)
    sale_page.check_title_women_page('Women Sale')


def test_correct_url(sale_page):
    sale_page.open()
    sale_page.current_url_is('https://magento.softwaretestingboard.com//sale.html')
