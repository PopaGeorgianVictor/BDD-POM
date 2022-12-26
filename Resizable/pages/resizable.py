from selenium.webdriver.common.by import By
from Radios.pages.base_page import BasePage
from selenium.webdriver import ActionChains

class Resize(BasePage):

    RESIZE = (By.XPATH, '//*[@id="resizable"]/div[3]')

    def navigate_to_page(self):
        self.driver.get()

