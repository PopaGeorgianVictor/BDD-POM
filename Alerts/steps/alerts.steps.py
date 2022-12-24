from behave import *

@given("I am on '/alert_confirm_prompt' homepage")
def step_impl(context):
    context.dropdown_object.navigate_to_page()

@when("I click on  'Show an alert (html alert)' button")
def step_impl(context):
    context.alert_object.click_html_alert()

@then("Is displayed an alert message , 'This is alert using just html.'")
def step_impl(context):
    context.alert_object.msg_html_alert()

@when("I click on close icon , 'X'")
def step_impl(context):
    context.alert_object.close_html_alert()

@then("I am able to close this alert")
def step_impl(context):
    context.alert_object.check_closed_alert()

@when("I click on  'Show JavaScript Alert' button")
def step_impl(context):
    context.alert_object.click_js_alert()

@when("I click  on 'OK' button")
def step_impl(context):
    context.alert_object.js_alert_accept()

@then("I am able to close this alert")
def step_impl(context):
    context.alert_object.js_screenshot_accept_alert()

@when("I click on  'Show a Confirm Alert' button")
def step_impl(context):
    context.alert_object.click_js_confirm_alert()

@when("I click on  'Cancel' button")
def step_impl(context):
    context.alert_object. js_confirm_cancel_alert()

@then("I am able to close this alert and message 'Too bad!!! You would've loved it!' is displayed")
def step_impl(context):
    context.alert_object.js_confirm_cancel_alert_msg()