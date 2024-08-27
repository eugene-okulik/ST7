from playwright.sync_api import BrowserContext, Page, expect, Route
import re
import pytest
from time import sleep


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_viewport_size({'width': 1520, 'height': 980})
    return page


def test_req_title(page):

    def cheng_req(route: Route):
        response = route.fetch()
        # print(response.json())
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 15 про'
        sleep(3)
        print(response.json())
        route.fulfill(response=response, json=body)
        sleep(3)

    page.route('**/step0_iphone/**', cheng_req)
    page.goto('https://www.apple.com/shop/buy-iphone', wait_until='domcontentloaded')
    page.locator('.rf-hcard-img').first.click()
    sleep(2)
    check_title = page.locator('[id="rf-digitalmat-overlay-label-0"]').first.inner_text()
    assert check_title == 'яблокофон 15 про'
    print(check_title)