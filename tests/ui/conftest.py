from pathlib import Path

import pytest
from playwright.sync_api import Browser, BrowserContext, Page

from automation.app.ui import HomePage, LoginPage
from automation.core.config.settings import get_settings

AUTH_FILE = Path("auth.json")

AD_URL_PATTERNS = [
    "**/*googlesyndication.com/**",
    "**/*doubleclick.net/**",
    "**/*googleadservices.com/**",
    "**/*pagead2.googlesyndication.com/**",
    "**/*tpc.googlesyndication.com/**",
    "**/*admaster.cc/**",
    "**/*adservice.google.com/**",
]


def _abort(route) -> None:
    route.abort()


def _block_ads(context: BrowserContext) -> None:
    for pattern in AD_URL_PATTERNS:
        context.route(pattern, _abort)


def _block_ads_on_page(page: Page) -> None:
    for pattern in AD_URL_PATTERNS:
        page.route(pattern, _abort)


@pytest.fixture(scope="session")
def auth_storage_state(browser: Browser) -> Path:
    """Log in once per session and save cookies/localStorage for reuse."""
    context = browser.new_context()
    _block_ads(context)
    page = context.new_page()
    LoginPage(page).login()
    context.storage_state(path=str(AUTH_FILE))
    context.close()
    return AUTH_FILE


@pytest.fixture
def authenticated_home_page(browser: Browser, auth_storage_state: Path):
    """Fresh browser context that is already logged in."""
    context = browser.new_context(storage_state=str(auth_storage_state))
    _block_ads(context)
    page = context.new_page()
    page.goto(get_settings().base_url)
    yield HomePage(page)
    context.close()


@pytest.fixture(scope="function")
def login_page(page: Page):
    _block_ads_on_page(page)
    print("before_test")
    yield LoginPage(page)
    print("after_test")
