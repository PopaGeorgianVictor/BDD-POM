from selenium.common import NoSuchElementException
from DemoStore.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Login(BasePage):

    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    REMEMBER_ME = (By.ID, "rememberme")
    LOGIN_BTN = (By.NAME, "login")
    DASHBOARD = (By.LINK_TEXT, "Dashboard")

    def navigate_to_page(self):
        self.driver.get("http://demostore.supersqa.com/my-account/")

    def insert_email(self):
        self.driver.find_element(*self.EMAIL).send_keys("test123@gmail.com")

    def insert_password(self):
        self.driver.find_element(*self.PASSWORD).send_keys("6KTPNqcwUAe7PAD")

    def select_remember_me(self):
        self.driver.find_element(*self.REMEMBER_ME).click()

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def check_login(self):
        try:
            self.driver.find_element(*self.DASHBOARD)
            print('Log in successfully')

        except NoSuchElementException:
            print('Log in failed')
