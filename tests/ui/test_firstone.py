from playwright.sync_api import Browser, BrowserContext, Page, expect
import time


class TestFirstOne:
    def test_first_one(
        self, before_after_test, page: Page, context: BrowserContext, browser: Browser
    ):
        page.get_by_text("Redirect Link", exact=True).click()

        with page.expect_request() as er:
            page.get_by_text("200").click()

        response = er.value
        response.
