"""App-agnostic Playwright component wrapper. Product widgets belong in app/ui/components."""

from __future__ import annotations

from playwright.sync_api import Locator


class BaseComponent:
    """Thin wrapper scoped to a root ``Locator`` (nav, dialog, widget, etc.).

    Subclass in ``app/ui/components`` and resolve children via ``self.root``.
    """

    def __init__(self, root: Locator) -> None:
        self.root = root

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
