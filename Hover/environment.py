from Hover.pages.hover import Hover
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.hover_object = Hover()

def after_all(context):
    context.browser.close()