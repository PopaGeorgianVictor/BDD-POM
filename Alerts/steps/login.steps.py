from behave import *

@given("I am a user on demostore My account page")
def step_impl(context):
    context.login_object.navigate_to_page()