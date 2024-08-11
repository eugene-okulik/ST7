from ui_test_alex_v.utils.user_data import UserData


def test_registration_with_valid_data(create_account_page, my_account_page):
    valid_password = UserData.generate_password()
    create_account_page.open()
    create_account_page.fill_in_first_name(UserData.generate_firstname())
    create_account_page.fill_in_last_name(UserData.generate_firstname())
    create_account_page.fill_in_email(UserData.generate_email())
    create_account_page.fill_in_password(valid_password)
    create_account_page.fill_in_password_confirmation(valid_password)
    create_account_page.click_on_create_an_account_button()
    my_account_page.successful_registration_message_displayed_is('Thank you for registering with Main Website Store.')


def test_registration_with_invalid_email_address(create_account_page):
    valid_password = UserData.generate_password()
    create_account_page.open()
    create_account_page.fill_in_first_name(UserData.generate_firstname())
    create_account_page.fill_in_last_name(UserData.generate_firstname())
    create_account_page.fill_in_email("john_wick")
    create_account_page.fill_in_password(valid_password)
    create_account_page.fill_in_password_confirmation(valid_password)
    create_account_page.click_on_create_an_account_button()
    create_account_page.invalid_email_notification_message_displayed_is(
        'Please enter a valid email address (Ex: johndoe@domain.com).')


def test_registration_with_wrong_confirmation_password(create_account_page):
    create_account_page.open()
    create_account_page.fill_in_first_name(UserData.generate_firstname())
    create_account_page.fill_in_last_name(UserData.generate_firstname())
    create_account_page.fill_in_email(UserData.generate_email())
    create_account_page.fill_in_password(UserData.generate_password())
    create_account_page.fill_in_password_confirmation(UserData.generate_password())
    create_account_page.click_on_create_an_account_button()
    create_account_page.confirm_password_notification_message_displayed_is('Please enter the same value again.')


def test_product_sort_by_name(eco_page):
    eco_page.open()
    assert eco_page.sort_products_by_name()


def test_add_product_to_compare(eco_page, product_page, compare_page):
    eco_page.open()
    eco_page.choose_product()
    product_page.add_to_compare_product()
    product_title = product_page.get_product_title()
    product_page.go_to_comparison_list()
    assert compare_page.compared_product_title_displayed_is(product_title)


def test_add_product_to_wish_list_as_quest_user(eco_page, product_page, customer_login_page):
    eco_page.open()
    eco_page.choose_product()
    product_page.add_to_wish_list()
    assert customer_login_page.invalid_login_notification_message_displayed_is(
        'You must login or register to add items to your wishlist.'
    )


def test_proper_page_title(sale_page):
    sale_page.open()
    sale_page.title_page_is('Sale')


def test_women_sections_sale_presence(sale_page):
    sale_page.open()
    actual_sections =sale_page.get_section_titles()
    sale_page.ex


