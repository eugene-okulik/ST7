from selenium.webdriver.common.by import By


class CartLocators:
    PRODUCT_ROW = (By.XPATH, '(//div[@class="product-item-info"])[1])')
    PRODUCT = '(//div[@class="product-item-info"])'
    ADD_TO_COMPARE = '(//a[@aria-label = "Add to Compare"])'
    COMPARE_PRODUCTS = (By.XPATH, '//strong[@class="product-item-name"]')
    ADD_TO_WISH_LIST = '(//a[@aria-label = "Add to Wish List"])'
    WISH_LIST_ERROR = (By.XPATH, '//div[contains(text(),"You must login or register to add items to your wi")]')
    PRODUCT_IN_CARD = (By.XPATH, '//span[@itemprop="name"]')
    PRODUCT_PRICE_IN_CARD = (By.XPATH, '(//span[@class="price-wrapper "])[1]')


class SaleLocators:
    SALE_VERIFY_PAGE = (By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')
    WOMEN_DEALS = (By.XPATH, '//span[contains(text(),"Shop Women’s Deals")]')
    MEN_DEALS = (By.XPATH, '//span[contains(text(),"Shop Men’s Deals")]')
    VERIFY_OFF = (By.XPATH, '//strong[contains(text(),"20% OFF")]')
    WOMEN_PAGE_TITLE = (By.XPATH, '//span[contains(text(),"Women Sale")]')
    MEN_PAGE_TITLE = (By.XPATH, '//span[contains(text(),"Men Sale")]')


class RegisterLocators:
    PAGE_TITLE = (By.XPATH, '//span[contains(text(),"Create New Customer Account")]')
    FIRST_NAME = (By.XPATH, '//input[@id="firstname"]')
    LAST_NAME = (By.XPATH, '//input[@id="lastname"]')
    EMAIL = (By.XPATH, '//input[@id="email_address"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    CONFIRM_PASSWORD = (By.XPATH, '//input[@id="password-confirmation"]')
    BUTTON_CREATE_ACCOUNT = (By.XPATH, '//button[@title="Create an Account"]')
    # PASSWORD_CONFIRM_ERROR = (By.XPATH, '//div[@id="password-confirmation-error"]')
    PASSWORD_CONFIRM_ERROR = (By.XPATH, '//div[contains(text(), "Please enter the same value again.")]')


class AccountLocators:
    REG_SUCCESS = (By.XPATH, '//div[contains(text(),"Thank you for registering with Main Website Store.")]')
    PAGE_TITLE = (By.XPATH, '//span[contains(text(),"My Account")]')
    LOGGED_IN = (By.XPATH, '//span[@class="logged-in"]')
    CONTACT_INFORMATION = (By.XPATH, '//div[@class="box box-information"]')
