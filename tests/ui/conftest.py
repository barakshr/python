import pytest
from playwright.sync_api import Page

from automation.core.config import Settings


@pytest.fixture(scope="function")
def before_after_test(page: Page, settings: Settings):
    print("before_test")
    page.goto(settings.base_url)
    yield
    print("after_test")
