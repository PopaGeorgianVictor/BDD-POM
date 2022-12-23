from selenium.webdriver.common.by import By
from Dropdown.pages.base_page import BasePage
from selenium.webdriver.support.select import Select
import time

class Dropdown(BasePage):

    FIRST_DROPDOWN = (By.ID, 'coding-language-select')
    SECOND_DROPDOWN = (By.ID, "dropdownMenuButton")
    OPTION_DROPDOWN = (By.LINK_TEXT, "OVERVIEW")

    def navigate_to_page(self):
        self.driver.get()

    def click_first_dropdown(self):
        self.driver.find_element(*self.FIRST_DROPDOWN).click()

    def display_all_options_first_dropdown(self):
        dropdown = self.driver.find_element(*self.FIRST_DROPDOWN)
        dropdown_object = Select(dropdown)

        all_options = dropdown_object.options
        for option in all_options:
            print(option.text)

    def select_first_dropdown(self):
        dropdown = self.driver.find_element(*self.FIRST_DROPDOWN)
        dropdown_object = Select(dropdown)
        dropdown_object.select_by_value('Python')
        dropdown_object.select_by_value('Java')
        dropdown_object.select_by_value('PHP')
        dropdown_object.select_by_value('C#')
        dropdown_object.select_by_value('SQL')

    def click_second_dropdown(self):
        self.driver.find_element(*self.SECOND_DROPDOWN).click()

    def check_link(self):
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        print("Second window title = " + driver.title)

        try:
            driver.find_element(By.CSS_SELECTOR, "span[title='PORTOFOLIO']")
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")







