from behave import *

@given(" I am on '/dropdown' homepage")
def step_impl(context):
    context.home_page_object.navigate_to_page()

@when("I click on  '--Please choose an option--' from 'Coding Languages List'")
def step_impl(context):
    context.home_page_select_using_class()