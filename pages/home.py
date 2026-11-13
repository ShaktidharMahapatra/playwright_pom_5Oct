from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page):
        self.accountNDList = page.get_by_role("link", name="Hello, sign in Account & Lists")
        self.searchTextBox = page.get_by_role("searchbox", name="Search Amazon.in")


    def clickOnAccountNdList(self):
        self.accountNDList.click()

    def validateTheVisibilityOfSearchBox(self):
        expect(self.searchTextBox).to_be_visible()