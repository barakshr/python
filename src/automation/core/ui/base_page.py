"""App-agnostic Playwright page wrapper. Product locators belong in app/ui/pages."""

from __future__ import annotations

from typing import Literal, TypeVar

from playwright.sync_api import Locator, Page
from automation.core.ui.base_actions import BaseActions

TPage = TypeVar("TPage", bound="BasePage")


class BasePage(BaseActions):
    """Thin wrapper around a Playwright ``Page``.

    Holds the page (and optional base URL) and exposes common interactions.
    Subclass in ``app/ui/pages`` with product-specific locators and actions.
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    def as_page(self, page_cls: type[TPage]) -> TPage:
        """Wrap the same Playwright page as another page object."""
        return page_cls(self.page)

    def wait_for_load_state(
        self,
        state: Literal["load", "domcontentloaded", "networkidle"] = "load",
    ) -> None:
        self.page.wait_for_load_state(state)

    def wait_for_url(self, url: str) -> None:
        self.page.wait_for_url(url)

    def screenshot(self, path: str) -> bytes:
        """Capture a screenshot to ``path``. Failure attachment belongs in reporting."""
        return self.page.screenshot(path=path)
