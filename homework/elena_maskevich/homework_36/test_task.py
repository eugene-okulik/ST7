import json
from playwright.sync_api import BrowserContext, Page, Route, expect, APIResponse
import pytest
import re


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    return page


def test_change_request(page):

    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        print(body['body']['digitalMat'][0]['familyTypes'][0]['productName'])
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон'
        body = json.dumps(body)
        route.fulfill(response=response, body=body)

    page.route(re.compile('/api/digital-mat'), change_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('(//h3[@class="rf-hcard-content-title"])[1]').click()
    new_text = page.locator('(//h2[@class="rf-digitalmat-overlay-header typography-manifesto"])[1]')
    expect(new_text).to_have_text('яблокофон')
