from behave import *

@given("I am on '/radio_btn' page")
def step_impl(context):
    context.dropdown_object.navigate_to_page()

@then("'Rock FM' button is selected by default")
def step_impl(context):
    context.dropdown_object.display_all_options_first_dropdown()