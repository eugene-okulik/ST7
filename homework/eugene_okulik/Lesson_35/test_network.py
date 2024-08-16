from playwright.sync_api import BrowserContext, Page, Request

import pytest
import re


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


def test_listen(page):

    def print_request(request: Request):
        print('REQUEST:', request.url, request.post_data)

    page.on('request', print_request)
    page.on('response', lambda response: print('RESPONSE:', response.status, response.url))
    page.goto('https://www.qa-practice.com/')


def test_catch_response(page):
    page.goto('https://www.airbnb.ru/')
    # with page.expect_response('**/autosuggestions**')
    with page.expect_response(re.compile('/autosuggestions')) as response_event:
        page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()
        response = response_event.value

    print(response)
    assert response.json()['show_nearby'] is False
