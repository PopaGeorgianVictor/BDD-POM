from selenium.webdriver.common.by import By
from BDD.pages.base_page import Base_page

class Home_page(Base_page)
    DROPDOWN_CLASS= (By.ID, 'coding-language-select')
    DROPDOWN_CSS = (By.ID, "dropdownMenuButton")
    OPTION_CSS = (By.XPATH, '//*[@id="dropdowns"]/div[2]/div/ul/li[4]/a')

    def navigate_to_page(self):
        self.driver.get()