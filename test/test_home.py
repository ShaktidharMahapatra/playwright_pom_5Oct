import re
from playwright.sync_api import Page, expect


def test_validate_UI_for_home(page: Page, amazonNavigation):
    expect(page.get_by_role("link", name="Amazon.in")).to_be_visible()
    expect(page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()
    expect(page.get_by_role("link", name="items in cart")).to_be_visible()
