from behave import *

@given("I am on '/radio_btn' page")
def step_impl(context):
    context.dropdown_object.navigate_to_page()

@then("'Rock FM' button is selected by default")
def step_impl(context):
    context.dropdown_object.default_is_selected()

@given("I select radio buttons one by one")
def step_impl(context):
    context.dropdown_object.click_all_btn()

@then("I can select any button")
def step_impl(context):
    context.dropdown_object.click_all_btn()

