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

    page.route(re.compile(''), change_req)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('[data-trigger-id="digitalmat-1"]').click()
