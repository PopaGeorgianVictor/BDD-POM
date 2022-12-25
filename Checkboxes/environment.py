from Checkboxes.pages.alerts import Checkbox
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.alert_object = Checkbox()

def after_all(context):
    context.browser.close()