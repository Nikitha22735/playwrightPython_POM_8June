
import allure
from playwright.sync_api import sync_playwright, expect, Page
import pytest

# @pytest.fixture()
# def page():
#      with sync_playwright() as p:
#             browser = p.chromium.connect(f'wss://cdp.lambdatest.com/playwright?capabilities={json.dumps(capabilities)}')
#             context = browser.new_context(geolocation={"latitude":36.7783, "longitude":-119.4179}, permissions=["geolocation"])
#             page = context.new_page()
#             yield page
@pytest.fixture()
def page():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(storage_state="testData\\cookies.json")
            page = context.new_page()
            yield page

@pytest.fixture()
def page_noCookies():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            yield page

@pytest.fixture()
def navigateToAmazon(page: Page):
    page.goto("https://www.amazon.in/")
    # page.goto(os.getenv("url"))

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="failed screen",
                attachment_type=allure.attachment_type.PNG
            )



    
    