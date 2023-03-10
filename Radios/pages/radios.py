from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from Radios.pages.base_page import BasePage


class Radio(BasePage):
    LOCATOR_BY_VALUE = 'input[name="radio-stations"][value="{value}"]'
    RADIOS = (By.NAME, 'radio-stations')
    BTN1 = (By.CSS_SELECTOR, "input[value='magic fm']")
    BTN2 = (By.CSS_SELECTOR, "input[value='radio galaxy']")
    BTN3 = (By.CSS_SELECTOR, "input[value='europa fm']")
    BTN4 = (By.CSS_SELECTOR, "input[value='rock fm']")

    def navigate_to_page(self):
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/radio-btn")

    def default_is_selected(self):
        expected_default_value = 'rock fm'
        default_element = self.driver.find_element(By.CSS_SELECTOR,
                                                   self.LOCATOR_BY_VALUE.format(value=expected_default_value))
        assert default_element.is_selected(), f"The default value of {expected_default_value} is not selected."

    def click_all_btn(self):
        try:
            self.driver.find_element(*self.BTN1).click()
            print("Magic FM button is clickable")
        except WebDriverException:
            print("Magic FM button is not clickable")

        try:
            self.driver.find_element(*self.BTN2).click()
            print("Radio Galaxy button is clickable")
        except WebDriverException:
            print("Radio Galaxy button is not clickable")

        try:
            self.driver.find_element(*self.BTN3).click()
            print("Europa FM  button is clickable")
        except WebDriverException:
            print("Europa FM  button is not clickable")

        try:
            self.driver.find_element(*self.BTN4).click()
            print("Rock FM  button is clickable")
        except WebDriverException:
            print("Rock FM button is not clickable")

    def verify_number_of_radio_btn(self):
        expected_values = ['magic fm', 'radio galaxy', 'europa fm', 'rock fm']
        all_radios = self.driver.find_elements(*self.RADIOS)
        assert len(all_radios) == len(expected_values), "the number of radios does not match the expected." \
                                                        "Expected: {}, Actual: {}".format(len(expected_values),
                                                                                          len(all_radios))


