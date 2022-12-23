from selenium.webdriver.common.by import By
from Dropdown.pages.base_page import Base_page
from selenium.webdriver.support.select import Select

class Dropdown(BasePage):

    FIRST_DROPDOWN = (By.ID, 'coding-language-select')
    SECOND_DROPDOWN = (By.ID, "dropdownMenuButton")

    def navigate_to_page(self):
        self.driver.get()

    def click_first_dropdown(self):
        self.driver.find_element(*self.DROPDOWN_CLASS).click()

    def display_all_options_first_dropdown(self):
        dropdown = self.driver.find_element(*self.DROPDOWN_CLASS)
        dropdown_object = Select(dropdown)

        all_options = dropdown_object.options
        for option in all_options:
            print(option.text)

    def select_first_dropdown(self):
        dropdown = self.driver.find_element(*self.DROPDOWN_CLASS)
        dropdown_object = Select(dropdown)
        dropdown_object.select_by_value('Python')
        dropdown_object.select_by_value('Java')
        dropdown_object.select_by_value('PHP')
        dropdown_object.select_by_value('C#')
        dropdown_object.select_by_value('SQL')

    def click_second_dropdown(self):
        self.driver.find_element(*self.DROPDOWN_CLASS).click()

    def display_all_options_second_dropdown(self):
        dropdown = self.driver.find_element(*self.DROPDOWN_CLASS)
        dropdown_object = Select(dropdown)

        all_options = dropdown_object.options
        for option in all_options:
            print(option.text)

    def select_second_dropdown(self):
        dropdown = self.driver.find_element(*self.DROPDOWN_CLASS)
        dropdown_object = Select(dropdown)
        dropdown_object.select_by_value('Python')
        dropdown_object.select_by_value('Java')
        dropdown_object.select_by_value('PHP')
        dropdown_object.select_by_value('C#')
        dropdown_object.select_by_value('SQL')







