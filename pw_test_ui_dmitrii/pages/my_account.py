from pw_test_ui_dmitrii.pages.base_page import BasePage


class MyAccountPage(BasePage):
    page_url = '/customer/account/'

    def check_correct_account_information(self, *my_tuple):
        reg_information = self.find('//div[@class="box-content"]/p')
        for el in my_tuple:
            yield el in reg_information.inner_text()
