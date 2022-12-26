from Resizable.pages.resizable import Resize
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.radios_object = Resize()

def after_all(context):
    context.browser.close()
