from BDD.pages.dropdowns import Dropdown
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.dropdown_object = Dropdown()


def after_all(context):
    context.browser.close()