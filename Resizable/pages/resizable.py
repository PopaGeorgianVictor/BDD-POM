from selenium.webdriver.common.by import By
from Radios.pages.base_page import BasePage
from selenium.webdriver import ActionChains

class Resize(BasePage):

    RESIZE = (By.XPATH, '//*[@id="resizable"]/div[3]')
    ELEM_RESIZABLE = (By.ID, 'resizable')

    def navigate_to_page(self):
        self.driver.get()

    def resizable(self):
        ActionChains(self.driver).drag_and_drop_by_offset(self.driver.find_element(*self.RESIZE), 500, 500).perform()

    def check_resize(self):
        elem = self.driver.find_element(*self.ELEM_RESIZABLE)
        expected_size = {'height': 619, 'width': 619}
        actual_size = elem.size
        assert expected_size == actual_size, f"Error: expected: {expected_size}, actual: {actual_size}"

    def resize_back(self):
        ActionChains(self.driver).drag_and_drop_by_offset(self.driver.find_element(*self.RESIZE), -500, -500).perform()

