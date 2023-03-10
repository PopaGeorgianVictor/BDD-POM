import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from RightClick.pages.base_page import BasePage


class RightClick(BasePage):

    CLICK = (By.CSS_SELECTOR, "#contextMenu a")
    ELEM = (By.LINK_TEXT, 'PORTOFOLIO')

    def navigate_to_page(self):
        self.driver.get("https://github.com/PopaGeorgianVictor/SELENIUM-UnitTest/blob/master/right_click.py")

    def right_click(self):
        ActionChains(self.driver).context_click().perform()

    def menu_option(self):
        self.driver.get_screenshot_as_file('right_menu.png')

    def click_on_option(self):
        self.driver.find_element(*self.CLICK).click()

    def open_link(self):
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        print("Second window title = " + self.driver.title)

        try:
            self.driver.find_element(*self.ELEM)
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")