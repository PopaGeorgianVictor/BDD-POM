from selenium.webdriver.common.by import By
from Dropdown.pages.base_page import BasePage



class Alerts(BasePage):

    HTML_ALERT = (By.CSS_SELECTOR, "div#bootStrapAlertExample button")
    HTML_ALERT_TEXT = (By.ID, "bootStrapAlert")
    JS_ALERT = (By.CSS_SELECTOR, "div#jsAlertExample button")
    JS_CONFIRM = (By.CSS_SELECTOR, "div#jsConfirmExample button")
    JS_PROMPT = (By.CSS_SELECTOR, "div#jsPromptExample button")
    INSERTED_TEXT = "test"

    def click_html_alert(self):
        self.driver.find_element(*self.HTML_ALERT).click()

    def check_msg_html_alert(self):
        html_alert_text = self.driver.find_element(*self.HTML_ALERT_TEXT).text
        expected_text = "This is alert using just html."
        assert html_alert_text == expected_text, f"Error: expected: {expected_text}, actual: {html_alert_text}"




