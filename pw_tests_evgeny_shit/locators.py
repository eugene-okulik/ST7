class CreateAccountLocators:
    creat_acc_button = '//button[@type="submit" and @title="Create an Account"]'
    required_fields = '//*[text()="This is a required field."]'
    first_name_input = '#firstname'
    last_name_input = '#lastname'
    email_input = '#email_address'
    password_input = '#password'
    password_confirm_input = '#password-confirmation'
    first_name_required_alert = '#firstname-error'
    error_message = '//*[contains(@data-bind, "parent")]'


class EcoFriendlyLocators:
    cards_li = '//li[@class="item product product-item"]'
    cards_li_4 = '(//li[@class="item product product-item"])[4]'
    cards_4_title = '//h1[@class="page-title"]'
    span_card = '#product-price-1882'


class SaleLocators:
    card_man_sale = '//a[@class="block-promo sale-mens"]'
    men_sale_title = '#page-title-heading'
    luma_gear_steal = '//strong[@class="title" and contains(text(), "Luma")]'
