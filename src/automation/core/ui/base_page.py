"""App-agnostic Playwright page wrapper. Product locators belong in app/ui/pages."""

from __future__ import annotations

from typing import Literal, TypeVar

from playwright.sync_api import Locator, Page

TPage = TypeVar("TPage", bound="BasePage")


class BasePage:
    """Thin wrapper around a Playwright ``Page``.

    Holds the page (and optional base URL) and exposes common interactions.
    Subclass in ``app/ui/pages`` with product-specific locators and actions.
    """

    def __init__(self, page: Page, base_url: str = "") -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    def as_page(self, page_cls: type[TPage]) -> TPage:
        """Wrap the same Playwright page as another page object."""
        return page_cls(self.page, base_url=self.base_url)

    def goto(self, path: str = "") -> None:
        """Navigate to an absolute URL or a path joined with ``base_url``."""
        if path.startswith(("http://", "https://")):
            url = path
        elif not path:
            url = self.base_url or "/"
        else:
            suffix = path if path.startswith("/") else f"/{path}"
            url = f"{self.base_url}{suffix}" if self.base_url else suffix
        self.page.goto(url)

    def click(self, locator: Locator) -> None:
        locator.click()

    def fill(self, locator: Locator, value: str) -> None:
        locator.fill(value)

    def check(self, locator: Locator) -> None:
        locator.check()

    def uncheck(self, locator: Locator) -> None:
        locator.uncheck()

    def select_option(
        self,
        locator: Locator,
        value: str | list[str] | None = None,
        *,
        label: str | list[str] | None = None,
        index: int | list[int] | None = None,
    ) -> None:
        locator.select_option(value=value, label=label, index=index)

    def press(self, locator: Locator, key: str) -> None:
        locator.press(key)

    def text_content(self, locator: Locator) -> str | None:
        return locator.text_content()

    def inner_text(self, locator: Locator) -> str:
        return locator.inner_text()

    def get_attribute(self, locator: Locator, name: str) -> str | None:
        return locator.get_attribute(name)

    def is_visible(self, locator: Locator) -> bool:
        return locator.is_visible()

    def is_enabled(self, locator: Locator) -> bool:
        return locator.is_enabled()

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
