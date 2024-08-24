from playwright.sync_api import BrowserContext, Page, Route

import pytest


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    return page


def test_change_response(page):
    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 15 про'
        print(response.url)
        print(response.json())
        route.fulfill(response=response, json=body)

    page.route('**/step0_iphone/**', change_response)

    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('[data-trigger-id="digitalmat-1"]').click()
    expected_iphone_title = page.locator('//h2[@data-autom="DigitalMat-overlay-header-0-0"]').first.inner_text()
    assert expected_iphone_title == 'яблокофон 15 про'
