"""Login page for https://the-internet.herokuapp.com/login."""

from __future__ import annotations

from playwright.sync_api import Locator

from automation.core.ui import BasePage


class LoginPage(BasePage):
    """Form Authentication login page (locators + actions only)."""

    PATH = "/login"

    def open(self) -> None:
        self.goto(self.PATH)

    @property
    def username_input(self) -> Locator:
        return self.page.get_by_label("Username")

    @property
    def password_input(self) -> Locator:
        return self.page.get_by_label("Password")

    @property
    def login_button(self) -> Locator:
        return self.page.get_by_role("button", name="Login")

    @property
    def flash_message(self) -> Locator:
        return self.page.locator("#flash")

    def fill_username(self, username: str) -> None:
        self.fill(self.username_input, username)

    def fill_password(self, password: str) -> None:
        self.fill(self.password_input, password)

    def click_login(self) -> None:
        self.click(self.login_button)

    def login(self, username: str, password: str) -> None:
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
