import os

import pytest

from pages.homePage import home
from pages.loginPage import loginPage
from utils.jsonHandling import jsonHandling

@pytest.mark.login
def test_positiveLogin_validaCreds(page,navigateToAmazon):
    homePageObj = home(page)
    loginPageObj = loginPage(page)
    homePageObj.clickOnAccountsndList()   
    # loginPageObj.enterEmailValue("trainingplaywright@gmail.com")
    loginPageObj.enterEmailValue(os.getenv("data_usn"))
    loginPageObj.enterEmailValue(os.getenv("data_usn2"))
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw("Welcome@04")
    loginPageObj.clickOnContinueBtn()
    homePageObj.validateVisibilityOfSeachBox()
    # data = jsonHandling("testData\\creds.json")
    # page.locator().select_option(data["positiveCreds"]["username"])