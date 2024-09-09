import random as r
import string as s

default_name = 'Dmitrii'
default_surname = 'Kiselev'
default_email = f'{"".join(r.choices(s.ascii_lowercase, k=5))}@yandex.ru'
name = 'ria Bikram Pant'


def test_new_customer_account_creation(create_account_page, my_account_page):
    create_account_page.open()
    create_account_page.fill_name_input(default_name)
    create_account_page.fill_surname_input(default_surname)
    create_account_page.fill_email_input(default_email)
    create_account_page.fill_password_input()
    create_account_page.fill_password_confirmation()
    create_account_page.scroll_page()
    create_account_page.push_create_account_button()
    assert my_account_page.check_correct_account_information(default_name, default_surname, default_email)


def test_without_name(create_account_page):
    create_account_page.open()
    create_account_page.fill_surname_input(default_surname)
    create_account_page.fill_email_input(default_email)
    create_account_page.fill_password_input()
    create_account_page.fill_password_confirmation()
    create_account_page.scroll_page()
    create_account_page.push_create_account_button()
    assert create_account_page.check_required_field()


def test_incorrect_password_confirmation(create_account_page):
    create_account_page.open()
    create_account_page.fill_name_input(default_name)
    create_account_page.fill_surname_input(default_surname)
    create_account_page.fill_email_input(default_email)
    create_account_page.fill_password_input()
    create_account_page.fill_password_confirmation('11')
    create_account_page.push_create_account_button()
    assert create_account_page.check_incorrect_password_to_confirm()


def test_opening_eco_product_page(eco_products_page, product_page):
    eco_products_page.open()
    eco_products_page.choose_eco_product(name)
    product_page.open_eco_product(eco_products_page.eco_product_page_url)
    product_page.check_opened_correct_product_page(name)


def test_unverified_adding_to_favorite(eco_products_page, login_page):
    eco_products_page.open()
    eco_products_page.move_attention_to_eco_supply(name)
    eco_products_page.click_to_favorite()
    assert login_page.check_unverified_action_opened()


def test_sorting_by_price(eco_products_page):
    eco_products_page.open()
    eco_products_page.sorting_by_('#sorter', 'price')  # почему-то не всегда переключение срабатывало(
    assert eco_products_page.check_order_by_price('.price')


def test_sales_page_opened(sales_page):
    sales_page.open()
    assert sales_page.check_sale_page_opened()


def test_luma_gear_offer(sales_page, deals_page):
    text = 'Gear'
    sales_page.open()
    sales_page.go_to_deal_page(text)
    assert deals_page.check_opened_correct_page(text)


def test_men_offer(sales_page, deals_page):
    text = 'Men'
    sales_page.open()
    sales_page.go_to_deal_page(text)
    assert deals_page.check_opened_correct_page(text)


def test_women_offer(sales_page, deals_page):
    sales_page.open()
    sales_page.go_to_deal_page('Pristine prices on pants, tanks and bras')
    assert deals_page.check_opened_correct_page('Women')