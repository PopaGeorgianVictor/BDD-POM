from behave import *

@given("I am on '/PRESENTATION-SITE/' page")
def step_impl(context):
    context.search_object.navigate_to_page()

@when("I hovering after 'OVERVIEW' menu")
def step_impl(context):
    context.hover_object.hovering()

@then("'OVERVIEW' menu is displayed")
def step_impl(context):
    context.hover_object.hovering()

@when("I click on 'Portofolio'")
def step_impl(context):
    context.hover_object.hovering()

@then("A new link are opened")
def step_impl(context):
    context.hover_object.click()