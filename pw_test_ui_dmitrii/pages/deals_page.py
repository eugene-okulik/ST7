from pw_test_ui_dmitrii.pages.base_page import BasePage


class DealsPage(BasePage):

    def check_opened_correct_page(self, text):
        return text in self.find('//span[@data-ui-id="page-title-wrapper"]').inner_text()
