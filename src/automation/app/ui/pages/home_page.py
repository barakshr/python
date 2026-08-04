from __future__ import annotations

from automation.core.ui import BasePage
from playwright.sync_api import Locator


class HomePage(BasePage):
    @property
    def search_input(self) -> Locator:
        return self.page.locator("twotabsearchtextbox")

    @property
    def search_button(self) -> Locator:
        return self.page.locator("#nav-search-submit-button")

    def search_item(self, text: str) -> None:
        self.click(self.search_input)
        self.fill(text)
        self.click(self.search_button)
