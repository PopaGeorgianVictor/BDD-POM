from behave import *

@given("I am on '/search_bar' page")
def step_impl(context):
    context.search_object.navigate_to_page()

@when("In the search bar input I type 'LISTS'")
def step_impl(context):
    context.search_object.search_for_elem()

@then("Specific results are displayed")
def step_impl(context):
    context.search_object.search_for_elem()