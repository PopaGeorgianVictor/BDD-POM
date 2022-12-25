from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

class Hover(unittest.TestCase):
    MENU = (By.CSS_SELECTOR,"#container a")
    PORTOFOLIO = (By.LINK_TEXT, "Portofolio")
    ELEM = (By.LINK_TEXT, "PORTOFOLIO")

    def hovering(self):
        menu = self.driver.find_element(*self.MENU)
        action = ActionChains(self.driver)
        action.move_to_element(menu).perform()
        link = self.driver.find_element(*self.PORTOFOLIO)
        action.move_to_element(link).click().perform()