from framework.app import App
from selenium import webdriver

# set up function that is called before any tests are run
def before_all(context):
    if context.config.userdata['browser'] == 'firefox':
        app = App(webdriver.Firefox())
    context.app = app

# teardown function that is called after tests are run
def after_all(context):
    context.app.quit_browser()
