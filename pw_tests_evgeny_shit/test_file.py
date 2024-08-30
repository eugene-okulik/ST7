def test_account_page_open(create_account_page):
    create_account_page.open()
    assert create_account_page.current_url_is_('https://magento.softwaretestingboard.com/customer/account/create/')


def test_click_submit_button(create_account_page):
    create_account_page.open()
    create_account_page.click_submit_button()
    assert create_account_page.number_of_required_fields_is_(5)


def test_send_keys_first_name(create_account_page):
    create_account_page.open()
    create_account_page.fill_in_reg_form('test', 'test', 'test@mail.com', 'QWe123321eWq')
    create_account_page.wait_for_error_message()
    assert create_account_page.error_message_text_is_(
        'There is already an account with this email address. '
        'If you are sure that it is your email address, '
        'click here to get your password and access your account.'
    )


def test_cards_count(eco_friendly_page):
    eco_friendly_page.open()
    assert eco_friendly_page.number_of_cards_on_page_is_(12)


def test_card_price(eco_friendly_page):
    eco_friendly_page.open()
    assert eco_friendly_page.product_daria_bikram_pant_price_is_('$40.80')


def test_click_card(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.click_on_card_bella_tank()
    assert eco_friendly_page.current_url_is_('https://magento.softwaretestingboard.com/bella-tank.html')
    assert eco_friendly_page.visible_card_title_is_('Bella Tank')


def test_title_page(sale_page):
    sale_page.open()
    assert sale_page.title_page_is_('Sale')


def test_click_man_sale_card(sale_page):
    sale_page.open()
    sale_page.click_on_man_sale_card()
    assert sale_page.current_url_is_('https://magento.softwaretestingboard.com/promotions/men-sale.html')
    assert sale_page.is_men_sale_title_visible()


def test_visible_title(sale_page):
    sale_page.open()
    assert sale_page.is_title_luma_gear_steal_visible()
