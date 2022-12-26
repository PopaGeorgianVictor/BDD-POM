import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Radios.pages.base_page import BasePage


class iFrames(BasePage)

    WITHOUT_FRAME = (By.ID, 'btnOutFrame')
    OF_FRAME = (By.CSS_SELECTOR, "div[id='link'] li:nth-child(1) a:nth-child(1)")
    FRAMES = (By.TAG_NAME, 'iframe')