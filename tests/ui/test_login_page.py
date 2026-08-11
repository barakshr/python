"""UI tests for the Form Authentication login page."""

from time import sleep
import pytest

from automation.app.ui import HomePage, LoginPage


@pytest.mark.ui
@pytest.mark.smoke
class TestLoginPage:
    def test_check_products(self, authenticated_home_page: HomePage):
        products_page = authenticated_home_page.top_bar_component.goto_products(via_link=True)
        products_page.check_url("https://automationexercise.com/products")
        sleep(4)

    def test_check_prod(self, authenticated_home_page: HomePage):
        products_page = authenticated_home_page.top_bar_component.goto_products(via_link=True)
        products_page.check_url("https://automationexercise.com/products")
        sleep(4)

    @pytest.mark.skip
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

    def test_login(self, login_page: LoginPage):
        login_page.login()
        pass
