from behave import *

@given("I am on  '/iFrame' page")
def step_impl(context):
    context.dropdown_object.navigate_to_page()