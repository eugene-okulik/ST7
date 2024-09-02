from pw_test_alex_v.pages.base_page import BasePage


class ComparePage(BasePage):

    def compared_product_title_displayed_is(self, message_text: str) -> bool:
        notification_message = self.find(".base").inner_text()
        return notification_message == message_text
