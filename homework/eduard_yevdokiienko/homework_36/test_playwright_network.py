from playwright.sync_api import BrowserContext, Page, Route, expect


def test_change_response(page: Page, context: BrowserContext):

    def subst_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 15 про'
        route.fulfill(response=response, json=body)

    page.route('**/step0_iphone/**', subst_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('(//h3[@class="rf-hcard-content-title"])[1]').click()
    req_text = page.locator('(//h2[@id="rf-digitalmat-overlay-label-0"])[1]')
    expect(req_text).to_contain_text('яблокофон 15 про')
