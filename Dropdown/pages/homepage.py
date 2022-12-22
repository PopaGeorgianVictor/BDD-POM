from selenium.webdriver.common.by import By
from BDD.pages.base_page import Base_page

class Home_page(Base_page)
    DROPDOWN_CLASS= (By.ID, 'coding-language-select')
    DROPDOWN_CSS = (By.ID, "dropdownMenuButton")
    OPTION_CSS = (By.XPATH, '//*[@id="dropdowns"]/div[2]/div/ul/li[4]/a')
    SITE_BTN = (By.CSS_SELECTOR, "span[title='PORTOFOLIO']")

    def navigate_to_page(self):
        self.driver.get()

    def select_using_class(self):


    def select_option(self):
        dropdown_object.select_by_value('Python')
        dropdown_object.select_by_value('Java')
        dropdown_object.select_by_value('PHP')
        dropdown_object.select_by_value('C#')
        dropdown_object.select_by_value('SQL')

    def check_all_option_class(self):
        options = self.driver.find_elements(*self.DROPDOWN_CLASS)
        for option in options:
            print(option.text)

    def select_using_css(self):
        self.driver.find_element(*self.DROPDOWN_CSS).click()
        self.driver.find_element(*self.OPTION_CSS).click()
        try:
            self.driver.find_element(*self.SITE_BTN)
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")


