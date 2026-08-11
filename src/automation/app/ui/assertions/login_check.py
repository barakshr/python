from logging import log
from automation.app.ui import LoginPage
from playwright.sync_api import Locator, Page, expect

from automation.core.ui import BasePage


class LoginCheck:
    @property
    def error_login(self) -> Locator:
        return self.page.locator("form[action='/login'] p")

    def __init__(self, login_page: BasePage):
        self.login_page = login_page
        self.page = login_page.page

    def assert_login_falied(self):
        expect(self.error_login).to_have_text("Your email or password is incorrect!")
        pass

    def assert_login_success(self):
        expect(self.page).to_have_url("https://automationexercise.com/")
