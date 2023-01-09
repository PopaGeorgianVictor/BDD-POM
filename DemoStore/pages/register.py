from DemoStore.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Register(BasePage):

    EMAIL = (By.ID, "reg_email")
    PASSWORD = (By.ID, "reg_password")
    REGISTER_BTN = (By.NAME, "register")
    ERROR_MSG = (By.XPATH, "//div[@id='content']//li[1]")
    DASHBOARD = (By.LINK_TEXT, "Dashboard")
    PASSWORD_HINT = (By.CSS_SELECTOR, ".woocommerce-password-hint")

    def navigate_to_page(self):
        self.driver.get("http://demostore.supersqa.com/my-account/")


    def insert_email(self):
        self.driver.find_element(*self.EMAIL).send_keys("test123@gmail.com")

    def insert_password(self):
        self.driver.find_element(*self.PASSWORD).send_keys("6KTPNqcwUAe7PAD")

    def click_on_register(self):
        self.driver.find_element(*self.REGISTER_BTN).click()

    def check_register(self):
        try:
            self.driver.find_element(*self.DASHBOARD)
            print('Registered successfully')

        except NoSuchElementException:
            print('Registration has not been completed')

    def invalid_email(self):
        self.driver.find_element(*self.EMAIL).send_keys("test")
        error = self.driver.find_element(*self.ERROR_MSG).text
        expected_text = 'Error: Please provide a valid email address.'
        assert error == expected_text, f"Error: expected: {expected_text}, actual: {hint}"


    def password_hint(self):
        self.driver.find_element(*self.PASSWORD).send_keys("1a")
        hint = self.driver.find_element(*self.PASSWORD_HINT).text
        expected_text = 'Hint: The password should be at least twelve characters long. To make it stronger, use upper and lower case letters, numbers, and symbols like ! " ? $ % ^ & ).'
        assert hint == expected_text, f"Error: expected: {expected_text}, actual: {hint}"