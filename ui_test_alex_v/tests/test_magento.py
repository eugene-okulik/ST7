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
