from Alerts.pages.alerts import Alerts
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.alert_object = Alerts()

def after_all(context):
    context.browser.close()