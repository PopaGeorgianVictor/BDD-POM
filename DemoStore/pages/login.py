from DemoStore.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Login(BasePage):

    EMAIL = (By.ID, "reg_email")
    PASSWORD = (By.ID, "reg_password")
    REGISTER_BTN = (By.NAME, "register")
    ERROR_TEXT = (By.XPATH,"//div[@id='content']//li[1]")

    def navigate_to_page(self):
        self.driver.get("http://demostore.supersqa.com/my-account/")

    def insert_email(self):
        self.driver.find_element(*self.EMAIL).send_keys("test123@gmail.com")

    def insert_password(self):
        self.driver.find_element(*self.PASSWORD).send_keys("6KTPNqcwUAe7PAD")