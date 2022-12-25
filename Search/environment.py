from Search.pages.search import Search
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.search_object = Search()


def after_all(context):
    context.browser.close()