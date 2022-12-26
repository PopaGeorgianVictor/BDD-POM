import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Radios.pages.base_page import BasePage


class Frames(BasePage):

    WITHOUT_FRAME = (By.ID, 'btnOutFrame')
    OF_FRAME = (By.CSS_SELECTOR, "div[id='link'] li:nth-child(1) a:nth-child(1)")
    FRAMES = (By.TAG_NAME, 'iframe')

    def navigate_to_page(self):
        self.driver.get()


    def click_outside_iFrame(self):
        self.driver.find_element(*self.WITHOUT_FRAME).click()

    def alert_outside_iFrame(self):
        alert = self.driver.switch_to.alert
        assert alert.text == 'Just Clicked Outside iFrame', "Should've gotten outside message"
        alert.accept()

    def inside_iFrame(self):
        self.driver.switch_to.frame('myFrame1')
        self.driver.find_element(*self.OF_FRAME).click()
        print('I clicked in frame')
        time.sleep(3)
        print("Second window title = " + self.driver.title)

        try:
            self.driver.find_element(*self.OF_FRAME)
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")

    def test_len_frames(self):
        frames = self.driver.find_elements(*self.FRAMES)
        for frame in frames:
            print(frame.get_attribute("id"))
        print(len(frames))