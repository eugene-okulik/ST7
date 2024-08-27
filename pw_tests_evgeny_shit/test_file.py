from pw_tests_evgeny_shit.locators import CreateAccountLocators as loc, SaleLocators as sale_loc, \
    EcoFriendlyLocators as eco_loc


def test_account_page_open(create_account_page):
    create_account_page.open()
    assert create_account_page.is_current_url('https://magento.softwaretestingboard.com/customer/account/create/')


def test_click_submit_button(create_account_page):
    create_account_page.open()
    create_account_page.click_element(loc.creat_acc_button)
    assert create_account_page.number_of_items_is(5)


def test_send_keys_first_name(create_account_page):
    create_account_page.open()
    create_account_page.fill_in_form('test', 'test', 'test@mail.com', 'QWe123321eWq')
    create_account_page.wait_for_element_visible(loc.error_message)
    assert create_account_page.error_message_text_is('There is already an account with this email address. '
                                                     'If you are sure that it is your email address, '
                                                     'click here to get your password and access your account.')


def test_cards_count(eco_friendly_page):
    eco_friendly_page.open()
    assert eco_friendly_page.number_of_items_is(12)


def test_card_price(eco_friendly_page):
    eco_friendly_page.open()
    assert eco_friendly_page.is_equal(eco_loc.span_card, '$40.80')


def test_click_card(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.click_element(eco_loc.cards_li_4)
    assert eco_friendly_page.is_current_url('https://magento.softwaretestingboard.com/bella-tank.html')
    assert eco_friendly_page.is_element_visible(eco_loc.cards_4_title)
    assert eco_friendly_page.is_equal(eco_loc.cards_4_title, 'Bella Tank')


def test_title_page(sale_page):
    sale_page.open()
    assert sale_page.is_title_page('Sale')


def test_click_man_sale_card(sale_page):
    sale_page.open()
    sale_page.click_element(sale_loc.card_man_sale)
    assert sale_page.is_current_url('https://magento.softwaretestingboard.com/promotions/men-sale.html')
    assert sale_page.is_element_visible(sale_loc.men_sale_title)
    assert sale_page.is_title_page('Men Sale')


def test_visible_title(sale_page):
    sale_page.open()
    assert sale_page.is_element_visible(sale_loc.luma_gear_steal)
