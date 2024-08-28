class CreateAccount:
    first_name_loc = '#firstname'
    last_name_loc = '#lastname'
    email_loc = '#email_address'
    password_loc = '#password'
    password_confirmation_loc = '#password-confirmation'
    click_button_account = '//button[@type="submit" and @title="Create an Account"]'
    thank_message = '//*[contains(@data-bind, "parent")]'
    error_message = '//*[contains(@data-bind, "parent")]'
    spase_input = 'firstname-error'


class EcoFriendly:
    cards_number = '(//li[@class="item product product-item"])[1]'
    price = '//*[@data-price-amount="40"]'
    card_title = '//span[@class="base"]'


class SalePage:
    title_sale = '//span[@class="base"]'
    button_shop = '//span[@class="more button"]'
    title_women_page = '//span[@class="base"]'
