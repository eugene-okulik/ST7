from playwright.sync_api import Page, expect, Route, BrowserContext
import pytest
import re


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    return page


def test_1_alert(page):

    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 15 про'
        route.fulfill(response=response, json=body)

    page.route(re.compile('shop/api/digital-mat'), change_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role('button', name='Take a closer look - iPhone 15 Pro & iPhone 15 Pro Max').click()
    expect(page.locator('#rf-digitalmat-overlay-label-0').nth(0)).to_have_text('яблокофон 15 про')
    page.get_by_role("button", name="Next", exact=True).click()
