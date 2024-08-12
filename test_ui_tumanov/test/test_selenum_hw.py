from test_ui_tumanov.pages.locators import (first_name_loc, last_name_loc, email_loc,
                                            password_loc, password_confirmation_loc,
                                            click_button_account)


def test_create_account(create_account, check_fio_email):
    create_account.open()
    create_account.input_met(first_name_loc, "Vite")
    create_account.input_met(last_name_loc, "Tuma")
    create_account.input_met(email_loc, 'testt@bk.com')
    create_account.input_met(password_loc, '123456zZz#!!')
    create_account.input_met(password_confirmation_loc, '123456zZz#!!')
    create_account.click_button(click_button_account)
    check_fio_email.customer_account()
