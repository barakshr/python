from math import exp
from playwright.sync_api import Locator, Page, expect


class BaseAssertion:
    def __init__(self, page: Page):
        self.page = page

    def assert_text(self, locator: Locator):
        expect(locator).to_have_text("Your email or password is incorrect!")
