from behave import *


@given("I am on '/checkbox' page")
def step_impl(context):
    context.checkboxes_object.navigate_to_page()

@then("Number of checkboxes is as expected")
def step_impl(context):
    context.checkboxes_object.check_number_checkbokes()