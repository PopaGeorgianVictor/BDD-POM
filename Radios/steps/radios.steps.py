from behave import *

@given("I am on '/radio_btn' page")
def step_impl(context):
    context.dropdown_object.navigate_to_page()