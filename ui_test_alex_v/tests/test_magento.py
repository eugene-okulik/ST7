from ui_test_alex_v.utils.user_data import UserData


def test_registration_with_valid_data(create_account_page, my_account_page):
    create_account_page.fill_in_first_name(UserData.generate_firstname())
    create_account_page.fill_in_last_name(UserData.generate_firstname())
    create_account_page.fill_in_email(UserData.generate_email())
    create_account_page.fill_in_password(UserData.generate_password())
    create_account_page.fill_in_password_confirmation(UserData.generate_password())
    create_account_page.click_on_create_an_account_button()
    my_account_page.successful_registration_message_displayed_is('Thank you for registering with Main Website Store.')
