from behave import *

@given("I am on  '/iFrame' page")
def step_impl(context):
    context.iframes_object.navigate_to_page()

@when("I click on outside frames button")
def step_impl(context):
    context.iframes_object.click_outside_iFrame()