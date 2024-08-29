class CartLocators:
    PRODUCT_ROW = '(//div[@class="product-item-info"])[1])'
    PRODUCT = '(//div[@class="product-item-info"])'
    ADD_TO_COMPARE = '(//a[@aria-label = "Add to Compare"])'
    COMPARE_PRODUCTS = '//strong[@class="product-item-name"]'
    ADD_TO_WISH_LIST = '(//a[@aria-label = "Add to Wish List"])'
    WISH_LIST_ERROR = '//div[contains(text(),"You must login or register to add items to your wi")]'
    PRODUCT_IN_CARD = '//span[@itemprop="name"]'
    PRODUCT_PRICE_IN_CARD = '(//span[@class="price-wrapper "])[1]'


class SaleLocators:
    SALE_VERIFY_PAGE = '//span[@data-ui-id="page-title-wrapper"]'
    WOMEN_DEALS = '//span[contains(text(),"Shop Women’s Deals")]'
    MEN_DEALS = '//span[contains(text(),"Shop Men’s Deals")]'
    VERIFY_OFF = '//strong[contains(text(),"20% OFF")]'
    WOMEN_PAGE_TITLE = '//span[contains(text(),"Women Sale")]'
    MEN_PAGE_TITLE = '//span[contains(text(),"Men Sale")]'


class RegisterLocators:
    PAGE_TITLE = '//span[contains(text(),"Create New Customer Account")]'
    FIRST_NAME = '//input[@id="firstname"]'
    LAST_NAME = '//input[@id="lastname"]'
    EMAIL = '//input[@id="email_address"]'
    PASSWORD = '//input[@id="password"]'
    CONFIRM_PASSWORD = '//input[@id="password-confirmation"]'
    BUTTON_CREATE_ACCOUNT = '//button[@title="Create an Account"]'
    PASSWORD_CONFIRM_ERROR = '//div[contains(text(), "Please enter the same value again.")]'


class AccountLocators:
    REG_SUCCESS = '//div[contains(text(),"Thank you for registering with Main Website Store.")]'
    PAGE_TITLE = '//span[contains(text(),"My Account")]'
    LOGGED_IN = '//span[@class="logged-in"]'
    CONTACT_INFORMATION = '//div[@class="box box-information"]'
