from Checkboxes.pages.checkboxes import Checkbox
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.checkboxes_object = Checkbox()

def after_all(context):
    context.browser.close()