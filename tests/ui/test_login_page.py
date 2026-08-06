"""UI tests for the Form Authentication login page."""

from automation.app.ui import HomePage
import pytest
from playwright.sync_api import expect

# Demo credentials from https://the-internet.herokuapp.com/login
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


@pytest.mark.ui
@pytest.mark.smoke
class TestLoginPage:
    def test_flow(self, home_page: HomePage) -> None:
        home_page.search_component.search_item("pen")
        pass
