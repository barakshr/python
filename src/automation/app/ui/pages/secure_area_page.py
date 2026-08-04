"""Secure area page shown after a successful login."""

from __future__ import annotations

from playwright.sync_api import Locator

from automation.core.ui import BasePage
from automation.app.ui.pages.exemple_page import ExamplePage


class SecureAreaPage(BasePage):
    """Post-login secure area (locators + actions only)."""

    PATH = "/secure"

    @property
    def flash_message(self) -> Locator:
        return self.page.locator("#flash")

    @property
    def example_link(self) -> Locator:
        return self.page.get_by_role("link", name="example")

    @property
    def logout_link(self) -> Locator:
        return self.page.get_by_role("link", name="Logout")

    def logout(self) -> None:
        self.click(self.logout_link)

    def click_exemple(self) -> ExamplePage:
        self.example_link()
        return ExamplePage(self.page)
