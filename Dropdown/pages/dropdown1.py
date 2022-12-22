from selenium.webdriver.common.by import By
from BDD.pages.base_page import Base_page

class Home_page(Base_page)
    DROPDOWN_CLASS= (By.ID, 'coding-language-select')
    DROPDOWN_CSS = (By.ID, "dropdownMenuButton")
    OPTION_CSS = (By.XPATH, '//*[@id="dropdowns"]/div[2]/div/ul/li[4]/a')
    SITE_BTN = (By.CSS_SELECTOR, "span[title='PORTOFOLIO']")

    def navigate_to_page(self):
        self.driver.get()

    def select(self):
        my_dropdown = self.driver.find_element(*self.DROPDOWN_CLASS)
        dropdown_object = Select(my_dropdown)
        dropdown_object.select_by_value('Python')
        dropdown_object.select_by_value('Java')
        dropdown_object.select_by_value('PHP')
        dropdown_object.select_by_value('C#')
        dropdown_object.select_by_value('SQL')

    def check_all_option(self):
        options = self.driver.find_elements(*self.DROPDOWN_CLASS)
        for option in options:
            print(option.text)



