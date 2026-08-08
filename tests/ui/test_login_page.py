"""UI tests for the Form Authentication login page."""

from automation.app.ui import HomePage, LoginPage
import pytest
from playwright.sync_api import expect

# Demo credentials from https://the-internet.herokuapp.com/login
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


@pytest.mark.ui
@pytest.mark.smoke
class TestLoginPage:
    def test_login(self, login_page: LoginPage):
        login_page.login()
        home_page = login_page.as_page(HomePage)
        products_page = home_page.top_bar_component.goto_products()
