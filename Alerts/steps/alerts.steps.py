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