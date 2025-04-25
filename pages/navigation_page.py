from playwright.async_api import async_playwright, expect, Page
from utils import config

class NavigationPage:
    def __init__(self, page: Page):
        self.page = page  # Store the Playwright page object
    
    async def open_selenium_dropdown(self):
        selenium_button = self.page.locator("text=Selenium")
        expect(selenium_button).to_be_visible()
        selenium_button.click()

    async def navigate_selenium_dropdown(self):
        # Click the "Selenium" button to open the dropdown
        self.page.goto(config.BASE_URL)
        self.page.click("text=Selenium")
        # List of menu items and expected titles
        menu_items = {
            "Flash Movie Demo": "Flash Movie Demo",
            "Radio & Checkbox Demo": "Radio Button & Check Box Demo",
            "Table Demo": "Table Demo"
        }

        for item_text, expected_page_title in menu_items.items():
            # Click each dropdown item
            self.page.wait_for_selector(f"text={item_text}")  # Ensure the element is present
            self.page.click(f"text={item_text}")
            # Verify the page title
            assert self.page.title() == expected_page_title, f"Title mismatch for {item_text}! Expected: {expected_page_title}, Found: {self.page.title()}"

            # Take a screenshot of each visited page
            self.page.screenshot(path=f"screenshots/{item_text.lower().replace(' ', '_')}.png")

            self.page.click("text=Selenium")

        
