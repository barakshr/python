"""UI tests for the Form Authentication login page."""

import re
import pytest
from playwright.sync_api import expect

from automation.app.ui import LoginPage, SecureAreaPage

# Demo credentials from https://the-internet.herokuapp.com/login
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


@pytest.mark.ui
@pytest.mark.smoke
class TestLoginPage:
    def test_successful_login(self, login_page: LoginPage) -> None:
        login_page.open()
        login_page.login(USERNAME, PASSWORD)
        secure_page = login_page.as_page(SecureAreaPage)
        example_page = secure_page.click_exemple()

        expect(secure_page.page).to_have_url(re.compile(r".*/secure"))
        expect(secure_page.flash_message).to_contain_text("You logged into a secure area!")

    def test_fail_login(self, login_page: LoginPage) -> None:
        login_page.open()
        login_page.login("", "")

        expect(login_page.page).to_have_url(re.compile(r".*/login"))
        expect(login_page.flash_message).to_contain_text("Your username is invalid!")
