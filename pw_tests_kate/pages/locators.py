class Locators:
    # Account Page Locators
    PASSWORD_FIELD = '//input[@type="password" and @title="Password"]'
    PASSWORD_STRENGTH_WEAK = '//span[@id="password-strength-meter-label"]'
    EMAIL_FIELD = '#email_address'
    CREATE_BUTTON = 'button[title="Create an Account"]'
    INVALID_EMAIL_ERROR = '#email_address-error'
    FIRST_NAME_FIELD = '#firstname'
    LAST_NAME_FIELD = '#lastname'
    CONFIRM_PASSWORD_FIELD = '#password-confirmation'
    SUCCESS_CONFIRMATION = 'div.message-success.success.message'

    # Eco-friendly Page Locators
    COMPARE_ICON = '(//a[@class="action tocompare" and @title="Add to Compare"])[5]'
    BRA_ITEM = '//img[@class="product-image-photo" and @alt="Electra Bra Top"]'
    COMPARED_ITEMS = '//strong[@class="product-item-name"]'
    TANK_ITEM = '//img[@class="product-image-photo" and @alt="Bella Tank"]'
    WISHLIST_ICON = '(//a[@class="action towishlist" and @title="Add to Wish List"])[4]'
    ERROR_MESSAGE = '[role="alert"]'
    LIST_VIEW_ICON = 'a.modes-mode.mode-list'
    LIST_VIEW_PAGINATION = '(//span[@class="toolbar-number"])[2]'

    # Sale Page Locators
    LUMA_GEAR_LINK = '//span[@class="more icon" and text()="Shop Luma Gear"]'
    HEADER = '//span[@class="base" and @data-ui-id="page-title-wrapper"]'
    BOTTLE_ICON = '//img[@class="product-image-photo" and @alt="Affirm Water Bottle "]'
    ADD_TO_CART_ICON = '(//button[@type="submit" and @title="Add to Cart"])[3]'
    CART_NUMBER = '//span[@class="counter-number" and text()="1"]'
    BRAS_AND_TANKS_LINK = '//a[text()="Bras & Tanks"]'
