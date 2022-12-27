from behave import *

@given("I am on '/radio_btn' page")
def step_impl(context):
    context.resize_object.navigate_to_page()

@when("I pull the edges element for resize")
def step_impl(context):
    context.resize_object.resizable()

@then("I can resize the element")
def step_impl(context):
    context.resize_object.check_resize()