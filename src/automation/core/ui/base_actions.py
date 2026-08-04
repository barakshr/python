from playwright.sync_api import Locator, Page


class BaseActions:
    def __init__(self, page: Page) -> None:
        self.page = page

    def fill(self, locator: Locator, value: str) -> None:
        locator.fill(value)

    def click(self, locator: Locator) -> None:
        locator.click()

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
