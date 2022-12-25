from Dropdown.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
class Search(BasePage):

    SEARCH_BAR = (By.ID, "myInput")
    ELEM = (By.LINK_TEXT, "LISTS")