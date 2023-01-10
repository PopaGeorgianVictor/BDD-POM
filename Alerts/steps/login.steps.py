from behave import *

@given("I am a user on demostore My account page")
def step_impl(context):
    context.login_object.navigate_to_page()

@when("I complete Username or email address field with a right address")
def step_impl(context):
    context.login_object.insert_email()

@when("I complete Password field with a right password")
def step_impl(context):
    context.login_object.insert_password()