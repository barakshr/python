"""UI tests for the Form Authentication login page."""

import pytest
from playwright.sync_api import Page

from automation.app.ui import HomePage, LoginPage
from automation.core.config.settings import get_settings


@pytest.mark.ui
@pytest.mark.smoke
class TestLoginPage:
    def test_check_products(self, authenticated_page: Page):
        authenticated_page.goto(get_settings().base_url)
        home_page = HomePage(authenticated_page)
        products_page = home_page.top_bar_component.goto_products(via_link=True)
        products_page.check_url("https://automationexercise.com/products")

    @pytest.mark.parametrize(
        "user, password",
        [
            pytest.param("user1@bla.com", "pass1", id="valid"),
            pytest.param("user1@bla.com", "bad", id="invalid"),
        ],
    )
    def test_check(self, login_page: LoginPage, user, password):
        login_page.login(user, password)
        home_page = login_page.as_page(HomePage)
        home_page.check_url("https://automationexercise.com/login")
