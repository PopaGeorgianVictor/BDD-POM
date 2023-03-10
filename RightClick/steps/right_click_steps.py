from behave import *

@given("I am on '/right_click_menu' page")
def step_impl(context):
    context.right_click_object.navigate_to_page()

@when("I perform a right click on page")
def step_impl(context):
    context.right_click_object.right_click()

@then("A right click menu opened")
def step_impl(context):
    context.right_click_object.menu_option()

@when("I click on option from menu")
def step_impl(context):
    context.right_click_object.click_on_option()

@then("A new link with related results are opened")
def step_impl(context):
    context.right_click_object.open_link()