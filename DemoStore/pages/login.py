from DemoStore.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Login(BasePage):

    EMAIL = (By.ID, "reg_email")
    PASSWORD = (By.ID, "reg_password")
    REGISTER_BTN = (By.NAME, "register")
    INVALID_EMAIL_TEXT = (By.CSS_SELECTOR,"//div[@id='content']//li[1]")



