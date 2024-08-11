from selenium.webdriver.common.by import By


class CreateAccountLocators:
    creat_acc_button = (By.XPATH, '//button[@type="submit" and @title="Create an Account"]')
    required_fields = (By.XPATH, '//*[text()="This is a required field."]')
    first_name_input = (By.ID, 'firstname')
    last_name_input = (By.ID, 'lastname')
    email_input = (By.ID, 'email_address')
    password_input = (By.ID, 'password')
    password_confirm_input = (By.ID, 'password-confirmation')
    first_name_required_alert = (By.ID, 'firstname-error')
    error_message = (By.XPATH, '//*[contains(@data-bind, "parent")]')


class EcoFriendlyLocators:
    cards_li = (By.XPATH, '//li[@class="item product product-item"]')
    cards_li_4 = (By.XPATH, '(//li[@class="item product product-item"])[4]')
    cards_4_title = (By.XPATH, '//h1[@class="page-title"]')
    span_card = (By.ID, 'product-price-1882')


class SaleLocators:
    card_man_sale = (By.XPATH, '//a[@class="block-promo sale-mens"]')
    men_sale_title = (By.ID, 'page-title-heading')
    luma_gear_steal = (By.XPATH, '//strong[@class="title" and contains(text(), "Luma")]')
