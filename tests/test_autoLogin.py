import re
from playwright.sync_api import Page, expect, sync_playwright


def cookiegeneartion():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.get_by_role("textbox", name="Username").fill("admin")
        page.get_by_role("textbox", name="Username").press("Tab")
        page.get_by_role("textbox", name="Password").fill("admin123")
        page.get_by_role("button", name="Login").click()
        page.wait_for_timeout(3000)
        context.storage_state(path="testData\\cookies.json")

def test_navigation():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(storage_state="testData\\cookies.json")
            page = context.new_page()
            page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
            page.wait_for_timeout(13000)

