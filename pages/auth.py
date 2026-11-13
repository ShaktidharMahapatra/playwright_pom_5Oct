class Auth:
    def __init__(self, page):
        self.enterEmailTextBox = page.get_by_role("textbox", name="Enter mobile number or email")
        self.continueBtn = page.get_by_role("button", name="Continue")
        self.password = page.get_by_role("textbox", name="Password")
        self.signInBtn = page.get_by_role("button", name="Sign in", exact=True)

    def enterEmail(self, userEmail):
        self.enterEmailTextBox.fill(userEmail)

    def clickOnContinue(self):
        self.continueBtn.click()

    def fillPassword(self):
        self.password.fill("Shakti123")

    def signInBtn(self):
        self.signInBtn.click()