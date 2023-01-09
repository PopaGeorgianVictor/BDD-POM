from DemoStore.pages.register import Login
from DemoStore.pages.register import Register
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.login_object = Login()
    context.register_object = Register()

def after_all(context):
    context.browser.close()