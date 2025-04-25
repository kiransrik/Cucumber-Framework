from behave import given, when, then
from playwright.async_api import async_playwright
from pages.navigation_page import NavigationPage

# The 'given' step to start the browser
@given("the user is on the homepage")
async def step_impl(context):
    async with async_playwright() as playwright:
        context.browser = await playwright.chromium.launch(headless=False)
        context.page = await context.browser.new_page()
        context.navigation = NavigationPage(context.page)
        await context.page.goto("https://www.guru99.com")

# The 'when' step for clicking the dropdown
@when("the user clicks the Selenium dropdown")
async def step_impl(context):
    await context.navigation.open_selenium_dropdown()

# The 'then' step for navigating and validating the dropdown items
@then("the user should be able to visit each Selenium subpage and see the correct title")
async def step_impl(context):
    await context.navigation.navigate_selenium_dropdown()
    await context.browser.close()
