from selenium.webdriver.common.by import By
from Radios.pages.base_page import BasePage
from selenium.webdriver import ActionChains

class Resize(BasePage):

    RESIZE = (By.XPATH, '//*[@id="resizable"]/div[3]')

    def navigate_to_page(self):
        self.driver.get()

    def resizable(self):
        ActionChains(self.driver).drag_and_drop_by_offset(self.driver.find_element(*self.RESIZE), 500, 500).perform()

    def resize_back(self):
        ActionChains(self.driver).drag_and_drop_by_offset(self.driver.find_element(*self.RESIZE), -500, -500).perform()

    def check_resize(self):
        expected = {'width': 1550, 'height': 830}
        actual = self.driver.get_window_size()
        assert expected == actual , f"Error: expected: {expected}, actual: {actual}"