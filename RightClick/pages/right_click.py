from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from Radios.pages.base_page import BasePage


class RightClick(BasePage):

    CLICK = (By.CSS_SELECTOR, "#contextMenu a")
    ELEM = (By.LINK_TEXT, 'PORTOFOLIO')