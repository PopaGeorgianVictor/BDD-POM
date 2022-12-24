from Radios.pages.radios import Radio
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.radios_object = Radio()

def after_all(context):
    context.browser.close()
