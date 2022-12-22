from BDD.pages.login_page import Home_page
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.home_page_object = Home_page()


def after_all(context):
    context.browser.close()