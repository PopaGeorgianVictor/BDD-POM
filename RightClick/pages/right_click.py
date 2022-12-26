import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Radios.pages.base_page import BasePage


class RightClick(BasePage):

    CLICK = (By.CSS_SELECTOR, "#contextMenu a")
    ELEM = (By.LINK_TEXT, 'PORTOFOLIO')

    def right_click(self):
        ActionChains(self.driver).context_click().perform()
        self.driver.find_element(*self.CLICK).click()
        print('I clicked on OVERVIEW')

    def click_on_option(self):
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        print("Second window title = " + self.driver.title)

        try:
            self.driver.find_element(*self.ELEM)
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")