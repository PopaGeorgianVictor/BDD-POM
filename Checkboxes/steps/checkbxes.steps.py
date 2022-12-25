from behave import *


@given("I am on '/checkbox' page")
def step_impl(context):
    context.checkboxes_object.navigate_to_page()

@then("Number of checkboxes is as expected")
def step_impl(context):
    context.checkboxes_object.check_number_checkbokes()

@when("I select one checkbox")
def step_impl(context):
    context.checkboxes_object.select_one_checkbox()

@then("I can select that particular checkbox")
def step_impl(context):
    context.checkboxes_object.select_one_checkbox()