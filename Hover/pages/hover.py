import time
from selenium.webdriver import ActionChains
from Search.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

class Hover(BasePage):

    MENU = (By.CSS_SELECTOR, "#container a")
    PORTOFOLIO = (By.LINK_TEXT, "Portofolio")
    ELEM = (By.LINK_TEXT, "PORTOFOLIO")

    def hovering(self):
        menu = self.driver.find_element(*self.MENU)
        action = ActionChains(self.driver)
        action.move_to_element(menu).perform()

    def click(self):
        self.driver.find_element(*self.PORTOFOLIO).click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        print("Second window title = " + self.driver.title)

        try:
            self.driver.find_element(*self.ELEM)
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")