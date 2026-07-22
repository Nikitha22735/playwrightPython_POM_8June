import re
import allure
from playwright.sync_api import expect, Page

class home():
    
    def __init__(self, page: Page):
        self.page = page
        self.searchBar = page.get_by_placeholder("Search Amazon.in")
        self.accountsndList = page.locator("//span[contains(text(),'Account & Lists')]")
        self.menuBtn = page.locator("#nav-hamburger-menu")
        self.searchBtn = page.locator("#nav-search-submit-button")
        self.searchBox = page.locator("input#twotabsearchtextbox")
        self.menuIcon = page.get_by_label("Open All Categories Menu")
        self.logo = page.locator("#nav-logo-sprites")

    @allure.step("validateVisibilityOfSearchbar")
    def validateVisibilityOfSearchbar(self):
        expect(self.searchBar).to_be_visible()

    
    @allure.step("validateVisibilityOfAccountsNdList")
    def validateVisibilityOfAccountsNdList(self):
        expect(self.accountsndList).to_be_visible()

    @allure.step("validateVisibilityOfMenuBar")
    def validateVisibilityOfMenuBar(self):
        expect(self.menuBtn).not_to_be_visible()

  
    @allure.step("enterSearchData")
    def enterSearchData(self, product):
        self.searchBar.fill(product)
    
    @allure.step("clickOnsearchBtn")
    def clickOnsearchBtn(self):
        self.searchBtn.click()

    
    @allure.step("waitingForSearchBoxToBeVisible")
    def waitingForSearchBoxToBeVisible(self):
        self.searchBox.wait_for(state="visible", timeout=50000)
    
    @allure.step("validateVisibilityOfSearchBox")
    def validateVisibilityOfSeachBox(self):
         expect(self.searchBox).to_be_visible()

    @allure.step("validateVisibilityOfAmazonLogo")
    def validateVisibilityOfAmazonLogo(self):
        expect(self.logo).to_be_visible()
    
    @allure.step("verifyTitle")
    def verifyTitle(self):
        expect(self.page).to_have_title(re.compile(r"Amazon\.in", re.IGNORECASE))
    
    @allure.step("validateVisibilityOfMenu")
    def validateThevisibityOfMenu(self):
        expect(self.menuIcon).to_be_visible()

    @allure.step("clickOnAccountsndList")
    def clickOnAccountsndList(self):
        self.accountsndList.click()

    
    @allure.step("enterSearchText")
    def enterSearchText(self, text):
        self.searchBox.fill(text)

    @allure.step("clickOnSearchBtn")
    def clickOnSearchBtn(self):
        self.searchBox.press("Enter")


