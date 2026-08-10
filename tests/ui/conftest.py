import pytest
from playwright.sync_api import Page

from automation.app.ui import LoginPage

pytest_plugins = ["automation.core.ui.pytest_plugin"]


@pytest.fixture(scope="function")
def login_page(page: Page):
    print("before_test")
    yield LoginPage(page)
    print("after_test")
