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