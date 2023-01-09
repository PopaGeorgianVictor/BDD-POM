from behave import *

@given("I am a user on demostore My account page")
def step_impl(context):
    context.register_object.navigate_to_page()

@when("I complete Email address field with a right address")
def step_impl(context):
    context.register_object.insert_email()

@when("I complete Password field which respects the security conditions")
def step_impl(context):
    context.register_object.insert_password()

@when("I click on Register button")
def step_impl(context):
    context.register_object.click_on_register()

@then("Register was successful")
def step_impl(context):
    context.register_object.check_register()

@when("I complete Email address field with a wrong address format")
def step_impl(context):
    context.register_object.invalid_email()

@when("I click on Register button")
def step_impl(context):
    context.register_object.click_on_register()

@then("I got the error message 'Please provide a valid email address'")
def step_impl(context):
    context.register_object.invalid_email_msg()

@when("I complete Email address field with an already registered address")
def step_impl(context):
    context.register_object.already_registered()

@when("I click on Register button")
def step_impl(context):
    context.register_object.click_on_register()

@then("I got the error message 'An account is already registered with your email address.'")
def step_impl(context):
    context.register_object.already_registered_msg()

@when("I complete password field but without respecting the security requirements")
def step_impl(context):
    context.register_object.password_hint()

@then('Hint: The password should be at least twelve characters long. To make it stronger, use upper and lower case letters, numbers, and symbols like ! " ? $ % ^ & ).')
def step_impl(context):
    context.register_object.password_hint_msg()