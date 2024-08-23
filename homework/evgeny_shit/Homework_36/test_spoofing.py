from playwright.sync_api import Route, Page


def test_modify_response(page: Page):
    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = "яблокофон 15 про"
        route.fulfill(response=response, json=body)

    page.route('**/step0_iphone/digitalmat', change_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('.rf-hcard.rf-hcard-40.rf-card-msgtag-orange.rf-hcard-centered-image').first.click()
    assert page.locator('#rf-digitalmat-overlay-label-0').first.inner_text() == "яблокофон 15 про"
