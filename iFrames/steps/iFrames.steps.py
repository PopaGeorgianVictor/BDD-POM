from behave import *

@given("I am on  '/iFrame' page")
def step_impl(context):
    context.iframes_object.navigate_to_page()

@when("I click on outside frames button")
def step_impl(context):
    context.iframes_object.click_outside_iFrame()

@then("An alert is displayed")
def step_impl(context):
    context.iframes_object.alert_outside_iFrame()

@when("I click on inside frames button")
def step_impl(context):
    context.iframes_object.click_inside_iFrame()