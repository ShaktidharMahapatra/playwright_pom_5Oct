from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page):
        self.accountNDList = page.get_by_role("link", name="Hello, sign in Account & Lists")
        self.searchTextBox = page.get_by_role("searchbox", name="Search Amazon.in")
        self.amazonLogo = page.get_by_role("link", name="Amazon.in")
        self.cartItem = page.get_by_role("link", name="items in cart")
        self.flag = page.locator("//div[text()='EN']")


    def clickOnAccountNdList(self):
        self.accountNDList.click()

    def validateTheVisibilityOfSearchBox(self):
        expect(self.searchTextBox).to_be_visible()

    def validateTheVisibilityOfAmazonLogo(self):
        expect(self.amazonLogo).to_be_visible()

    def validateTheVisibilityOfAddToCart(self):
        expect(self.cartItem).to_be_visible() 

    def validateTheVisibilityOfFlag(self):
        expect(self.flag).to_be_visible() 