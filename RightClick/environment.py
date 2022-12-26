from RightClick.pages.right_click import RightClick
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.right_click_object = RightClick()

def after_all(context):
    context.browser.close()
