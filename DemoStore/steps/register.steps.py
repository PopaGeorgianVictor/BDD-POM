from behave import *

@given("I am a user on demostore My account page")
def step_impl(context):
    context.register_object.navigate_to_page()