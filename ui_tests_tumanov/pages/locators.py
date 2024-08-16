from selenium.webdriver.common.by import By


class CreateAccount:
    first_name_loc = (By.ID, 'firstname')
    last_name_loc = (By.ID, 'lastname')
    email_loc = (By.ID, 'email_address')
    password_loc = (By.ID, 'password')
    password_confirmation_loc = (By.ID, 'password-confirmation')
    click_button_account = (By.XPATH, '//span[text()="Create an Account"]')
    thank_message = (By.XPATH, '//*[contains(@data-bind, "parent")]')
    error_message = (By.XPATH, '//*[contains(@data-bind, "parent")]')
    spase_input = (By.ID, 'firstname-error')


class EcoFriendly:
    cards_number = (By.XPATH, '(//li[@class="item product product-item"])[1]')
    price = (By.XPATH, '//*[@data-price-amount="40"]')
    card_title = (By.XPATH, '//span[@class="base"]')


class SalePage:
    title_sale = (By.XPATH, '//span[@class="base"]')
    button_shop = (By.XPATH, '//span[@class="more button"]')
    title_women_page = (By.XPATH, '//span[@class="base"]')
    jackets = (By.LINK_TEXT, 'Jackets')
    jackets_elements = (By.XPATH, '//span[@class="toolbar-number"]')
