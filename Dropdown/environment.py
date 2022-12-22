from BDD.pages.login_page import FirstDropdown
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.firts_dropdown_object = FirstDropdown()


def after_all(context):
    context.browser.close()