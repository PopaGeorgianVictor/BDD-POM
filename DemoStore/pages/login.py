from selenium.common import NoSuchElementException
from DemoStore.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Login(BasePage):

    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    REMEMBER_ME = (By.ID, "rememberme")
    LOGIN_BTN = (By.NAME, "login")
    DASHBOARD = (By.LINK_TEXT, "Dashboard")
    ERROR_MSG =(By.XPATH,"//div[@id='content']//li[1]")

    def navigate_to_page(self):
        self.driver.get("http://demostore.supersqa.com/my-account/")

    def insert_email(self):
        self.driver.find_element(*self.EMAIL).send_keys("test123@gmail.com")

    def insert_password(self):
        self.driver.find_element(*self.PASSWORD).send_keys("6KTPNqcwUAe7PAD")

    def select_remember_me(self):
        checkbox = self.driver.find_element(*self.REMEMBER_ME).click()
        assert checkbox.is_selected(), 'Checkbox not selected'

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def check_login(self):
        try:
            self.driver.find_element(*self.DASHBOARD)
            print('Log in successfully')

        except NoSuchElementException:
            print('Log in failed')

    def error_empty_email_field(self):
        error = self.driver.find_element(*self.ERROR_MSG).text
        expected_text = 'Error: Username is required.'
        assert error == expected_text, f"Error: expected: {expected_text}, actual: {error}"

    def error_empty_password_field(self):
        error = self.driver.find_element(*self.ERROR_MSG).text
        expected_text = 'Error: The password field is empty.'
        assert error == expected_text, f"Error: expected: {expected_text}, actual: {error}"

    def invalid_email(self):
        self.driver.find_element(*self.EMAIL).send_keys("abc123")
        error = self.driver.find_element(*self.ERROR_MSG).text
        expected_text = 'Error: The username abc123 is not registered on this site. If you are unsure of your username, try your email address instead.'
        assert error == expected_text, f"Error: expected: {expected_text}, actual: {error}"

    def invalid_password(self):
        self.driver.find_element(*self.PASSWORD).send_keys("abc123")
        error = self.driver.find_element(*self.ERROR_MSG).text
        expected_text = "Error: The password you entered for the email address test123@gmail.com is incorrect. Lost your password?"
        assert error == expected_text, f"Error: expected: {expected_text}, actual: {error}"