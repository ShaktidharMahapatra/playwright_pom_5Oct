import re
from playwright.sync_api import Page, expect
from pages.auth import Auth
from pages.home import HomePage


def test_validatePositiveLogin(page: Page, amazonNavigation):
    HomePageObj = HomePage(page)
    AuthObj = Auth(page)
    HomePageObj.clickOnAccountNdList()
    AuthObj.enterEmail("shakti.jeetu123@gmail.com")
    AuthObj.clickOnContinue()
    AuthObj.fillPassword("Shakti123")
    AuthObj.signInBtn()
    HomePageObj.validateTheVisibilityOfSearchBox()    
    

def test_validateNegativeLogin(page: Page, amazonNavigation):
    HomePageObj = HomePage(page)
    AuthObj = Auth(page)
    HomePageObj.clickOnAccountNdList()
    AuthObj.enterEmail("shakti.jeetu123@gmail.com")
    AuthObj.clickOnContinue()
    AuthObj.fillPassword("Shakti123")
    AuthObj.signInBtn()
    AuthObj.validateIncorrectPwMsg()

