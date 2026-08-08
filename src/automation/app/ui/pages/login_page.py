from __future__ import annotations
from automation.app.ui import HomePage
from automation.core.ui import BasePage
from automation.app.ui.components.search_component import SearchComponent
from automation.core.ui import BasePage
from playwright.sync_api import Locator
from playwright.sync_api import Page
from automation.core.config.settings import get_settings

import json


class LoginPage(BasePage):
    def __init__(self, page, from_setting_file: bool = True):
        super().__init__(page)
        if from_setting_file:
            page.goto(f"{get_settings().base_url}/login")

        self.cred = self.read_cred()

    def read_cred(self):
        with open("cred.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        return {"user": data["user"], "pass": data["pass"]}

    @property
    def email_input(self) -> Locator:
        return self.page.locator("[data-qa='login-email']")

    @property
    def password_input(self):
        return self.page.locator("[data-qa='login-password']")

    @property
    def login_button(self):
        return self.page.locator("[data-qa='login-button']")

    def fill_email(self, email: str = ""):
        if email:
            self.fill(self.email_input, email)
        else:
            self.fill(self.email_input, self.cred["user"])

    def fill_password(self, password: str = ""):
        if password:
            self.fill(self.password_input, password)
        else:
            self.fill(self.password_input, self.cred["pass"])

    def login(
        self,
        email: str = "",
        password: str = "",
    ):
        self.fill_email(email)
        self.fill_password(password)
        self.click(self.login_button)
