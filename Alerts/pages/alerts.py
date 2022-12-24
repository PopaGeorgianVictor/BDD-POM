from selenium.webdriver.common.by import By
from Dropdown.pages.base_page import BasePage


class Alerts(BasePage):

    HTML_ALERT = (By.CSS_SELECTOR, "#bootStrapAlertExample button")
    HTML_ALERT_TEXT = (By.ID, "bootStrapAlert")
    HTML_ALERT_CLOSE = (By.CSS_SELECTOR, ".btn-close")
    JS_ALERT = (By.CSS_SELECTOR, "#jsAlertExample button")
    JS_CONFIRM = (By.CSS_SELECTOR, "#jsConfirmExample button")
    RS_CONFIRM = (By.ID, 'userResponse1')
    JS_PROMPT = (By.CSS_SELECTOR, "#jsPromptExample button")
    RS_PROMPT = (By.ID, 'userResponse2')
    INSERTED_TEXT = "test"

    def navigate_to_page(self):
        self.driver.get()

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

        try:
            self.driver.find_element(*self.HTML_ALERT_CLOSE)
            print('Element still exist')

        except NoSuchElementException:
            print("Element does not exist, closed successfully")

    def js_alert_accept(self):
        js_alert = self.driver.switch_to.alert
        js_alert.accept()

    def click_js_confirm_alert(self):
        self.driver.find_element(*self.JS_CONFIRM).click()

    def js_confirm_accept_alert(self):
        js_confirm = self.driver.switch_to.alert
        js_confirm.accept()
        rs_message = self.driver.find_element(*self.RS_CONFIRM).text
        assert rs_message == 'Great! You will love it!', "Wrong message after accepting"

    def js_confirm_cancel_alert(self):
        js_confirm = self.driver.switch_to.alert
        js_confirm.dismiss()
        rs_message = self.driver.find_element(*self.RS_CONFIRM).text
        assert rs_message == "Too bad!!! You would've loved it!", "Wrong message after canceling"

    def click_js_prompt_alert(self):
        self.driver.find_element(*self.JS_PROMPT).click()

    def js_prompt_cancel_alert(self):
        js_prompt = self.driver.switch_to.alert
        js_prompt.dismiss()

    def test_js_prompt_accept_alert_without_text(self):
        js_prompt = self.driver.switch_to.alert
        js_prompt.accept()
        rs_message = self.driver.find_element(*self.RS_PROMPT).text
        expected_text = f"You have entered: none"
        assert rs_message == expected_text, f"Error: expected: {expected_text}, actual: {rs_message}"

    def test_js_prompt_accept_alert_with_text(self):
        js_prompt = self.driver.switch_to.alert
        js_prompt.send_keys(self.INSERTED_TEXT)
        js_prompt.accept()
        rs_message = self.driver.find_element(*self.RS_PROMPT).text
        expected_text = f"You have entered: {self.INSERTED_TEXT}"
        assert rs_message == expected_text, f"Error: expected: {expected_text}, actual: {rs_message}"




