from behave import *

@given("I am on '/dropdown' homepage")
def step_impl(context):
    context.first_dropdown_object_object.navigate_to_page()

@when("I click on  '--Please choose an option--' from 'Coding Languages List'")
def step_impl(context):
    context.first_dropdown_object.click()

@then("A dropdown menu opens with related options")
def step_impl(context):
    context.first_dropdown_object.display_all_options()

