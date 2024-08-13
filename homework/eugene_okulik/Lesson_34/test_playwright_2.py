from playwright.sync_api import Page, expect
from time import sleep


def test_by_test_id(page: Page):
    page.goto('https://www.airbnb.ru/')
    sleep(2)
    page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()
    sleep(3)


def test_by_locator(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    # basket = page.locator('.action.showcart')
    basket = page.locator('//*[@class="action showcart"]')
    basket.click()
    sleep(3)


def test_strength(page: Page):
    page.goto('https://magento.softwaretestingboard.com/customer/account/create/')
    input_field = page.locator('#password')
    # input_field.fill('skdjfhskdjfh')
    # input_field.press_sequentially('sdkfjhskd', delay=100)
    input_field.type('ksdjhfksjdfh')
    sleep(3)


def test_enabled_and_select(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/disabled')
    button = page.locator('#submit-id-submit')
    expect(button).to_be_disabled()
    page.locator('#id_select_state').select_option('enabled')
    expect(button).to_be_enabled()
    expect(button).to_have_text('Submit')


def test_wait(page: Page):
    page_url = 'https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html?product_list_order=price'
    page.goto(page_url)
    print(page.url)
    page.locator('[data-role="direction-switcher"]').first.click()
    print(page.url)
    expect(page).not_to_have_url(page_url)
    print(page.url)


def test_hover(page: Page):
    page.goto('https://magento.softwaretestingboard.com/men.html')
    men = page.locator('#ui-id-5')
    tops = page.locator('#ui-id-17')
    jackets = page.locator('#ui-id-19')
    men.hover()
    tops.hover()
    jackets.click()
    sleep(3)


def test_d_n_d(page: Page):
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_me = page.locator('#rect-draggable')
    drag_here = page.locator('#rect-droppable')
    drag_me.drag_to(drag_here)
    sleep(3)
    dropped_text = drag_here.locator('#text-droppable')
    expect(dropped_text).to_have_text('Dropped!')


def test_iframe(page: Page):
    page.goto('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = page.frame_locator('iframe')
    burger = iframe.locator('.navbar-toggler-icon')
    burger.click()
    sleep(3)
