import time

from .junk import Junk
from playwright.sync_api import Browser, BrowserContext, Page, expect


class TestFirstOne:
    def test_first_one(
        self, before_after_test, page: Page, context: BrowserContext, browser: Browser
    ):

        pass

    def test_junk(self):
        junk = Junk(name="barak")
        assert junk.name == "barak"
        # assert junk.age == 30
