from iFrames.pages.right_click import iFrames
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.iframes_object = iFrames()

def after_all(context):
    context.browser.close()
