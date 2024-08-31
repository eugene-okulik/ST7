from playwright.sync_api import Page, Route, BrowserContext, expect
import pytest
import re


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    return page


def test_change_response(page):

    def catch_iphone_15(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 15 про'
        route.fulfill(response=response, json=body)

    page.route(re.compile('/api/digital-mat'), catch_iphone_15)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role('button', name='Take a closer look - iPhone 15 Pro & iPhone 15 Pro Max').click()
    changed_response_text = page.locator('(//h2[@id="rf-digitalmat-overlay-label-0"])[1]')
    expect(changed_response_text).to_have_text('яблокофон 15 про')
