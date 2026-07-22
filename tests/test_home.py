
from playwright.sync_api import Page
import pytest

from pages.homePage import home

@pytest.mark.home
@pytest.mark.smoke
@pytest.mark.regression
def test_validating_the_home_screen_elements(page:Page,navigateToAmazon):
    homePageObj = home(page)
    homePageObj.validateVisibilityOfSearchbar()
    homePageObj.validateVisibilityOfAccountsNdList()
    homePageObj.validateVisibilityOfMenuBar()
    homePageObj.validateVisibilityOfAmazonLogo()

@pytest.mark.home
@pytest.mark.regression
def test_validate_the_home_page_title(page:Page,navigateToAmazon):
    homePageObj = home(page)
    homePageObj.verifyTitle()

@pytest.mark.home
@pytest.mark.regression
def test_validate_search_box_accepts_input(page:Page,navigateToAmazon):
    homePageObj = home(page)
    homePageObj.enterSearchData("iphone")
    homePageObj.validateVisibilityOfSeachBox()

