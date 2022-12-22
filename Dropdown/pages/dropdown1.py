from selenium.webdriver.common.by import By
from BDD.pages.base_page import Base_page

class Home_page(Base_page)

    DROPDOWN_CLASS= (By.ID, 'coding-language-select')

    def navigate_to_page(self):
        self.driver.get()

    def select(self):
        dropdown = self.driver.find_element(*self.DROPDOWN_CLASS)
        dropdown_object = Select(dropdown)
        dropdown_object.select_by_value('Python')
        dropdown_object.select_by_value('Java')
        dropdown_object.select_by_value('PHP')
        dropdown_object.select_by_value('C#')
        dropdown_object.select_by_value('SQL')

    def display_all_options(self):
        dropdown = self.driver.find_element(*self.DROPDOWN_CLASS)
        dropdown_object = Select(dropdown)

        all_options = dropdown_object.options
        for option in all_options:
            print(option.text)






