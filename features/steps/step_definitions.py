
from behave import given, when, then

@given('the web browser is currently open')
def open_generic_page(context):
    context.app.open('about:blank')

@given('the url "{url}" is currently open')
def ensure_page_open(context, url):
    context.app.open(url)

@given('the "{page}" page loads successfully')
def verify_page_load_given(context, page):
    if (page == 'home' or page == 'business' or page == 'article'):
        context.app.verify_page_load()

@when('the user navigates to url "{url}"')
def navigate_to_page(context, url):
    context.app.open(url)

@when('the user selects "{category}" from the navigation bar')
def select_category(context, category):
    context.app.select_category_from_nav_bar(category)

@when('the user selects article "{a}"')
def select_article_by_number(context, a):
    context.app.select_article_by_number(int(a))

@then('the "{page}" page loads successfully')
def verify_page_load_then(context, page):
    if (page == 'home' or page == 'business' or page == 'article'):
        context.app.verify_page_load()

@then('the page load time is under "{t}" milliseconds')
def verify_page_load_time(context, t):
    context.app.verify_page_load_time(int(t))

@then('the author name is populated')
def verify_author_name_populated(context):
    context.app.verify_author_name_populated()






