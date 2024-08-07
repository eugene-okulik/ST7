from test_ui_evgeny_shit.locators import creat_acc_button, required_fields, first_name_input, \
    last_name_input, email_input, password_input, password_confirm_input, error_message, cards_li, span_card, \
    cards_li_4, cards_4_title, card_man_sale, men_sale_title, luma_gear_steal

URL = 'https://magento.softwaretestingboard.com/customer/account/create/'
ECO_URL = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'
SALE_URL = 'https://magento.softwaretestingboard.com/sale.html'


def test_account_page_open(create_account_page):
    create_account_page.open(URL)
    assert create_account_page.is_current_url('https://magento.softwaretestingboard.com/customer/account/create/')


def test_click_submit_button(create_account_page):
    create_account_page.open(URL)
    create_account_page.click_element(creat_acc_button)
    assert create_account_page.is_correct_number_of_items(required_fields, 5)


def test_send_keys_first_name(create_account_page):
    create_account_page.open(URL)
    create_account_page.send_keys(first_name_input, 'test')
    create_account_page.send_keys(last_name_input, 'test')
    create_account_page.send_keys(email_input, 'test@mail.com')
    create_account_page.send_keys(password_input, 'QWe123321eWq')
    create_account_page.send_keys(password_confirm_input, 'QWe123321eWq')
    create_account_page.click_element(creat_acc_button)
    assert create_account_page.is_element_visible(error_message)


def test_cards_count(eco_friendly_page):
    eco_friendly_page.open(ECO_URL)
    assert eco_friendly_page.is_correct_number_of_items(cards_li, 12)


def test_card_price(eco_friendly_page):
    eco_friendly_page.open(ECO_URL)
    assert eco_friendly_page.is_equal(span_card, '$40.80')


def test_click_card(eco_friendly_page):
    eco_friendly_page.open(ECO_URL)
    eco_friendly_page.click_element(cards_li_4)
    assert eco_friendly_page.is_current_url('https://magento.softwaretestingboard.com/bella-tank.html')
    assert eco_friendly_page.is_element_visible(cards_4_title)
    assert eco_friendly_page.is_equal(cards_4_title, 'Bella Tank')


def test_title_page(sale_page):
    sale_page.open(SALE_URL)
    assert sale_page.is_title_page('Sale')


def test_click_man_sale_card(sale_page):
    sale_page.open(SALE_URL)
    sale_page.click_element(card_man_sale)
    assert sale_page.is_current_url('https://magento.softwaretestingboard.com/promotions/men-sale.html')
    assert sale_page.is_element_visible(men_sale_title)
    assert sale_page.is_title_page('Men Sale')


def test_visible_title(sale_page):
    sale_page.open(SALE_URL)
    assert sale_page.is_element_visible(luma_gear_steal)
