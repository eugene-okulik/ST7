import time
# import json
# import requests

from playwright.sync_api import BrowserContext, Page, Route, expect, APIResponse

import pytest
import re


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    return page


def test_change_request(page):

    def change_req(route: Route):
        url = route.request.url
        if 'filter3' in url:
            url = url.replace('&filter3=09z01', '')
            print(url)
        route.continue_(url=url)

    page.route(re.compile('/product/finder'), change_req)
    page.goto('https://www.samsung.com/au/smartphones/galaxy-z/')
    page.locator('[data-di-id="di-id-e1b2a925-25f273a3"]').click()
    time.sleep(3)
    page.locator('[for="checkbox-series09z01"]').click()
    time.sleep(5)


def test_change_response(page):

    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['temperature'] = '+28'
        body['icon'] = 'A2'
        # body = json.dumps(body)
        route.fulfill(response=response, json=body)

    page.route('**/pogoda/**', change_response)
    page.goto('https://www.onliner.by/')
    page.locator('[name="query"]').click()
    time.sleep(5)


def test_api(page):
    # response = requests.get('https://jsonplaceholder.typicode.com/posts/42')
    response = page.request.get('https://jsonplaceholder.typicode.com/posts/42')
    expect(response).to_be_ok()
    assert response.status == 200
    assert response.json()['id'] == 42


def test_catch_response(page):
    page.goto('https://www.airbnb.ru/')
    # with page.expect_response('**/autosuggestions**')
    with page.expect_response(re.compile('/autosuggestions')) as response_event:
        page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()
        response = response_event.value

    expect(APIResponse(response)).to_be_ok()
    print(response)
    assert response.json()['show_nearby'] is False
