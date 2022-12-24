from behave import *

@given("I am on '/alert_confirm_prompt' homepage")
def step_impl(context):
    context.dropdown_object.navigate_to_page()

@when("I click on  'Show an alert (html alert)' button")
def step_impl(context):
    context.alert_object.click_html_alert()