from selenium.webdriver.common.by import By
from Radios.pages.base_page import BasePage


class Radio(BasePage):
    LOCATOR_BY_VALUE = 'input[name="radio-stations"][value="{value}"]'
    RADIOS = (By.NAME, 'radio-stations')
    BTN1 = (By.CSS_SELECTOR, "input[value='magic fm']")
    BTN2 = (By.CSS_SELECTOR, "input[value='radio galaxy']")
    BTN3 = (By.CSS_SELECTOR, "input[value='europa fm']")
    BTN4 = (By.CSS_SELECTOR, "input[value='rock fm']")


    def default_is_selected(self):
        expected_default_value = 'rock fm'
        default_element = self.driver.find_element(By.CSS_SELECTOR,
                                                   self.LOCATOR_BY_VALUE.format(value=expected_default_value))
        assert default_element.is_selected(), f"The default value of {expected_default_value} is not selected."

    def click_all_btn(self):
        self.driver.find_element.click()
        self.driver.find_element.click()
        self.driver.find_element.click()
        self.driver.find_element.click()


