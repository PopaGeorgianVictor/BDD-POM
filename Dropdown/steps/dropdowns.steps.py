from behave import *

@given("I am on '/dropdown' homepage")
def step_impl(context):
    context.dropdown_object.navigate_to_page()

@when("I click on  '--Please choose an option--' from 'Coding Languages List'")
def step_impl(context):
    context.dropdown_object.click_first_dropdown()

@then("A dropdown menu opens with related options")
def step_impl(context):
    context.dropdown_object.display_all_options_first_dropdown()

@when("I select options one by one from dropdown")
def step_impl(context):
    context.dropdown_object.select_first_dropdown()

@then("I can select any option from dropdown")
def step_impl(context):
    context.dropdown_object.select_first_dropdown()