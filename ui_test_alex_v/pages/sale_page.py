from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from ui_test_alex_v.pages.base_page import BasePage


class SalePage(BasePage):
    page_url = '/sale.html'

    def get_section_titles(self):
        WebDriverWait(self.driver, 20).until(
            ec.visibility_of_all_elements_located((By.XPATH, "//ul[@class='items']//li/a"))
        )
        sections = self.driver.find_elements(By.XPATH, "//ul[@class='items']//li/a")
        section_titles = [section.text.strip() for section in sections]

        print(f"Found sections: {section_titles}")
        return section_titles

    def get_discount_value(self):
        discount_element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CLASS_NAME, "block-promo.sale-20-off"))
        )
        print(discount_element.text)
        return discount_element.text
