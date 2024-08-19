from playwright.sync_api import Page, expect


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    visible_after = page.locator('#visibleAfter')
    expect(visible_after).to_be_visible()
    color_change_button = page.locator("#colorChange")
    color_change_button.click()
