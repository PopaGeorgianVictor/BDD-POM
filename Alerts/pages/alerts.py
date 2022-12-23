from selenium.webdriver.common.by import By
from Dropdown.pages.base_page import BasePage
from selenium.webdriver.support.select import Select
import time

class Alerts(BasePage):

    HTML_ALERT = (By.CSS_SELECTOR, "div#bootStrapAlertExample button")
    HTML_ALERT_TEXT = (By.ID, "bootStrapAlert")
    JS_ALERT = (By.CSS_SELECTOR, "div#jsAlertExample button")
    JS_CONFIRM = (By.CSS_SELECTOR, "div#jsConfirmExample button")
    JS_PROMPT = (By.CSS_SELECTOR, "div#jsPromptExample button")
    INSERTED_TEXT = "test"



