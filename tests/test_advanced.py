from playwright.sync_api import sync_playwright

def dimensions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 600, "height": 1080})
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(2000)


def mobile():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(**p.devices['iPhone 12'])
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(2000)


def geolocation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(geolocation={"latitude":36.7783, "longitude":-119.4179}, permissions=["geolocation"])
        page = context.new_page()
        page.goto("https://browserleaks.com/geo")
        page.wait_for_timeout(12000)


def netWorkMocking():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 600, "height": 1080})
            page = context.new_page()
            context.set_offline(True)
            page.goto("https://testautomationpractice.blogspot.com/")
            page.wait_for_timeout(2000)

def iframes():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://demo.guru99.com/test/guru99home/")
            page.frame_locator("//iframe[contains(@src,'youtube')]").locator('(//button[@aria-label="Play video"])[1]').click()
            # //button[@aria-label="Pause video"]
            page.wait_for_timeout(3000)
            page.frame_locator("//iframe[contains(@src,'youtube')]").locator('//button[@aria-label="Pause video"]').click()
            page.wait_for_timeout(3000)

def ss():
      with sync_playwright() as p:
             browser = p.chromium.launch(headless=False)
             context = browser.new_context()
             page = context.new_page()
             page.goto("https://testautomationpractice.blogspot.com/")
             page.wait_for_timeout(2000)
            #  page.screenshot(full_page=True,path="ssfolder/ss2.png")
             page.locator('[onclick="toggleButton(this)"]').screenshot(path="ssfolder/strt.png")

##pip install pillow
from PIL import Image,ImageChops
def test_visualRegression():
      with sync_playwright() as p:
             browser = p.chromium.launch(headless=False)
             context = browser.new_context()
             page = context.new_page()
             img1 = Image.open("ss1.png")
             img2 = Image.open("ssfolder/ss1.png")
             diff = ImageChops.difference(img1, img2)
             print(diff)
             print(diff.getbbox())
             assert diff.getbbox() is None
     



        