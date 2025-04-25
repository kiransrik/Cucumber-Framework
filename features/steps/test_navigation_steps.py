from behave import given, when, then
from playwright.sync_api import sync_playwright, expect
from pages.navigation_page import NavigationPage
import time

@given("the user is on the homepage")
def step_impl(context):
    playwright = sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.navigation = NavigationPage(context.page)
    context.page.goto("https:///demo.guru99.com/popup.php")

@when("the user clicks the Selenium dropdown")
def step_impl(context):
    context.navigation.open_selenium_dropdown()

@then("the user should be able to visit each About subpage and see the correct title")
def step_impl(context):
    context.navigation.navigate_selenium_dropdown()
    context.browser.close()
