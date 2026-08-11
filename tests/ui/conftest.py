from pathlib import Path

import pytest
from playwright.sync_api import Browser, Page

from automation.app.ui import LoginPage

pytest_plugins = ["automation.core.ui.pytest_plugin"]

AUTH_FILE = Path("auth.json")


@pytest.fixture(scope="session")
def auth_storage_state(browser: Browser) -> Path:
    """Log in once per session and save cookies/localStorage for reuse."""
    context = browser.new_context()
    page = context.new_page()
    LoginPage(page).login()
    context.storage_state(path=str(AUTH_FILE))
    context.close()
    return AUTH_FILE


@pytest.fixture
def authenticated_page(browser: Browser, auth_storage_state: Path):
    """Fresh browser context that is already logged in."""
    context = browser.new_context(storage_state=str(auth_storage_state))
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="function")
def login_page(page: Page):
    print("before_test")
    yield LoginPage(page)
    print("after_test")
