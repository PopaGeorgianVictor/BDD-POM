from behave import *


@given("I am on '/alert_confirm_prompt' page")
def step_impl(context):
    context.dropdown_object.navigate_to_page()

