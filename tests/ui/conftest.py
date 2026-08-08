import pytest
from playwright.sync_api import Page

from automation.app.ui import LoginPage
from automation.core.config import Settings
from automation.app.ui import HomePage


@pytest.fixture(scope="function")
def before_after_test(page: Page, settings: Settings):
    print("before_test")
    yield
    print("after_test")


@pytest.fixture
def login_page(page: Page, settings: Settings, before_after_test: None):
    return LoginPage(page)
