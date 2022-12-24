from selenium.webdriver.common.by import By
from Radios.pages.base_page import BasePage


class Radio(BasePage):
    LOCATOR_BY_VALUE = 'input[name="radio-stations"][value="{value}"]'
    RADIOS = (By.NAME, 'radio-stations')





