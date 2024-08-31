from selenium.webdriver.common.by import By


class Locators:
    # Account Page Locators
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password" and @title="Password"]')
    PASSWORD_STRENGTH_WEAK = (By.XPATH, '//span[@id="password-strength-meter-label"]')
    EMAIL_FIELD = (By.ID, 'email_address')
    CREATE_BUTTON = (By.CSS_SELECTOR, 'button.action.submit.primary')
    INVALID_EMAIL_ERROR = (By.ID, 'email_address-error')
    FIRST_NAME_FIELD = (By.ID, 'firstname')
    LAST_NAME_FIELD = (By.ID, 'lastname')
    CONFIRM_PASSWORD_FIELD = (By.ID, 'password-confirmation')
    SUCCESS_CONFIRMATION = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')

    # Eco-friendly Page Locators
    COMPARE_ICON = (By.XPATH, '(//a[@class="action tocompare" and @title="Add to Compare"])[5]')
    BRA_ITEM = (By.XPATH, '//img[@class="product-image-photo" and @alt="Electra Bra Top"]')
    COMPARED_ITEMS = (By.XPATH, '//strong[@class="product-item-name"]')
    TANK_ITEM = (By.XPATH, '//img[@class="product-image-photo" and @alt="Bella Tank"]')
    WISHLIST_ICON = (By.XPATH, '(//a[@class="action towishlist" and @title="Add to Wish List"])[4]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[role="alert"]')
    LIST_VIEW_ICON = (By.XPATH, '//a[@class="modes-mode mode-list" and @id="mode-list"]')
    LIST_VIEW_PAGINATION = (By.XPATH, '(//span[@class="toolbar-number"])[2]')

    # Sale Page Locators
    LUMA_GEAR_LINK = (By.XPATH, '//span[@class="more icon" and text()="Shop Luma Gear"]')
    HEADER = (By.XPATH, '//span[@class="base" and @data-ui-id="page-title-wrapper"]')
    BOTTLE_ICON = (By.XPATH, '//img[@class="product-image-photo" and @alt="Affirm Water Bottle "]')
    ADD_TO_CART_ICON = (By.XPATH, '(//button[@type="submit" and @title="Add to Cart"])[3]')
    CART_NUMBER = (By.XPATH, '//span[@class="counter-number" and text()="1"]')
    BRAS_AND_TANKS_LINK = (By.XPATH, '//a[text()="Bras & Tanks"]')
