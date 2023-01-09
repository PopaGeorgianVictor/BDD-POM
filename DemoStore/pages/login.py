from selenium.common import NoSuchElementException
from DemoStore.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Login(BasePage):
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")




    def navigate_to_page(self):
        self.driver.get("http://demostore.supersqa.com/my-account/")
