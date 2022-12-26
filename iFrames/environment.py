from iFrames.pages.iFrames import Frames
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.iframes_object = Frames()

def after_all(context):
    context.browser.close()
