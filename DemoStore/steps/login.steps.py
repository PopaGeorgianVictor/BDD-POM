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

@when("I select checkbox  Remember me")
def step_impl(context):
    context.login_object.select_remember_me()

@then("The checkbox was selected")
def step_impl(context):
    context.login_object.select_remember_me()

@when("I click on Log in button")
def step_impl(context):
    context.login_object.click_login()

@then("I am able to log in")
def step_impl(context):
    context.login_object.check_login()

@then('I got the error message "Error: Username is required."')
def step_impl(context):
    context.login_object.error_empty_email_field()