from pw_test_ui_dmitrii.pages.base_page import BasePage


class LoginPage(BasePage):

    def check_unverified_action_opened(self):
        locator = '//div[@data-ui-id="message-error"]/div'
        return 'You must login or register to add items to your wishlist' in self.find(locator).inner_text()
