from behave import *

@given("I am on '/right_click_menu' page")
def step_impl(context):
    context.radios_object.navigate_to_page()