from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Alerts.pages.base_page import BasePage


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
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/alert_confirm_prompt")

    def click_html_alert(self):
        self.driver.find_element(*self.HTML_ALERT).click()

    def msg_html_alert(self):
        html_alert_text = self.driver.find_element(*self.HTML_ALERT_TEXT).text
        expected_text = "This is alert using just html."
        assert html_alert_text == expected_text, f"Error: expected: {expected_text}, actual: {html_alert_text}"

    def close_html_alert(self):
        self.driver.find_element(*self.HTML_ALERT_CLOSE).click()

    def check_closed_alert(self):
        try:
            self.driver.find_element(*self.HTML_ALERT_CLOSE)
            print('Element still exist')

        except NoSuchElementException:
            print("Element does not exist, closed successfully")

    def click_js_alert(self):
        self.driver.find_element(*self.JS_ALERT).click()

    def js_alert_accept(self):
        js_alert = self.driver.switch_to.alert
        js_alert.accept()

    def js_screenshot_accept_alert(self):
        self.driver.get_screenshot_as_file('screenshot_accept_alert.png')

    def click_js_confirm_alert(self):
        self.driver.find_element(*self.JS_CONFIRM).click()

    def js_confirm_accept_alert(self):
        js_confirm = self.driver.switch_to.alert
        js_confirm.accept()

    def js_confirm_accept_alert_msg(self):
        rs_message = self.driver.find_element(*self.RS_CONFIRM).text
        assert rs_message == 'Great! You will love it!', "Wrong message after accepting"

    def js_confirm_cancel_alert(self):
        js_confirm = self.driver.switch_to.alert
        js_confirm.dismiss()

    def js_confirm_cancel_alert_msg(self):
        rs_message = self.driver.find_element(*self.RS_CONFIRM).text
        assert rs_message == "Too bad!!! You would've loved it!", "Wrong message after canceling"

    def click_js_prompt_alert(self):
        self.driver.find_element(*self.JS_PROMPT).click()

    def js_prompt_cancel_alert(self):
        js_prompt = self.driver.switch_to.alert
        js_prompt.dismiss()

    def js_screenshot_cancel_prompt(self):
        self.driver.get_screenshot_as_file('screenshot_cancel_prompt.png')

    def js_prompt_accept_alert_without_text(self):
        js_prompt = self.driver.switch_to.alert
        js_prompt.accept()

    def js_accept_prompt_without_text_msg(self):
        rs_message = self.driver.find_element(*self.RS_PROMPT).text
        expected_text = f"You have entered: none"
        assert rs_message == expected_text, f"Error: expected: {expected_text}, actual: {rs_message}"

    def js_prompt_insert_text_accept(self):
        js_prompt = self.driver.switch_to.alert
        js_prompt.send_keys(self.INSERTED_TEXT)
        js_prompt.accept()

    def js_accept_prompt_with_text_msg(self):
        rs_message = self.driver.find_element(*self.RS_PROMPT).text
        expected_text = f"You have entered: {self.INSERTED_TEXT}"
        assert rs_message == expected_text, f"Error: expected: {expected_text}, actual: {rs_message}"




