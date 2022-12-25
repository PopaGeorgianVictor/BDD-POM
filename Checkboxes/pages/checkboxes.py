from Dropdown.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Checkbox(BasePage):
    TO_SELECT_VALUE = '21-40'
    LOCATOR_BY_VALUE = f'input[name="age-group-checkbox"][value="{TO_SELECT_VALUE}"]'
    MY_CHOICE = (By.CSS_SELECTOR, LOCATOR_BY_VALUE)
    ALL_CHECKBOXES = (By.NAME, 'age-group-checkbox')
