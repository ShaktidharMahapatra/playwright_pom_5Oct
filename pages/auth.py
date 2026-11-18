from playwright.sync_api import Page, expect

class Auth:
    def __init__(self, page):
        self.enterEmailTextBox = page.get_by_role("textbox", name="Enter mobile number or email")
        self.continueBtn = page.get_by_role("button", name="Continue")
        self.password = page.get_by_role("textbox", name="Password")
        self.signInBtnLocator = page.get_by_role("button", name="Sign in", exact=True)
        self.inCorrectPw = page.get_by_text("Your password is incorrect")

    def enterEmail(self, userEmail):
        self.enterEmailTextBox.fill(userEmail)

    def clickOnContinue(self):
        self.continueBtn.click()

    def fillPassword(self, userPw):
        self.password.fill(userPw)

    def signInBtn(self):
        self.signInBtnLocator.click()

    def validateIncorrectPwMsg(self):
        expect(self.inCorrectPw).to_be_visible()