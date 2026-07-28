import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function")
def before_after_test(page: Page):
    print("before_test")
    page.goto("https://the-internet.herokuapp.com")
    yield
    print("after_test")
