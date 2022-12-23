from selenium.webdriver.common.by import By
from Dropdown.pages.base_page import BasePage


class Alerts(BasePage):

    HTML_ALERT = (By.CSS_SELECTOR, "#bootStrapAlertExample button")
    HTML_ALERT_TEXT = (By.ID, "bootStrapAlert")
    HTML_ALERT_CLOSE = (By.CSS_SELECTOR, ".btn-close")
    JS_ALERT = (By.CSS_SELECTOR, "#jsAlertExample button")
    JS_CONFIRM = (By.CSS_SELECTOR, "#jsConfirmExample button")
    RS_MSG_CONFIRM = (By.ID, 'userResponse1')
    JS_PROMPT = (By.CSS_SELECTOR, "#jsPromptExample button")
    RS_MSG_PROMPT = (By.ID, 'userResponse2')
    INSERTED_TEXT = "test"

    def click_html_alert(self):
        self.driver.find_element(*self.HTML_ALERT).click()

    def msg_html_alert(self):
        html_alert_text = self.driver.find_element(*self.HTML_ALERT_TEXT).text
        expected_text = "This is alert using just html."
        assert html_alert_text == expected_text, f"Error: expected: {expected_text}, actual: {html_alert_text}"

    def close_html_alert(self):
        self.driver.find_element(*self.HTML_ALERT_CLOSE).click()

    def click_js_alert(self):
        self.driver.find_element(*self.JS_ALERT).click()

    def js_alert_accept(self):
        js_alert = self.driver.switch_to.alert
        js_alert.accept()

    def click_js_confirm_alert(self):
        self.driver.find_element(*self.JS_CONFIRM).click()

    def js_confirm_accept_alert(self):









