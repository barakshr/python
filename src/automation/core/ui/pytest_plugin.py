"""Pytest plugin for UI lifecycle hooks (screenshot on failure, etc.)."""

import pytest
from _pytest.fixtures import FixtureRequest
from automation.core.ui.screenshots import save_failure_screenshot
from pytest import TestReport


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Stash the test report on the item so fixtures can inspect pass/fail."""
    outcome = yield
    report: TestReport = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request: FixtureRequest):
    """After each UI test, save a screenshot if the test body failed."""
    yield
    rep: TestReport | None = getattr(request.node, "rep_call", None)
    if rep is None or not rep.failed:
        return

    # Prefer authenticated_page so we do not force creating a logged-out page.
    page = None
    for name in ("authenticated_page", "page"):
        if name in request.fixturenames:
            page = request.getfixturevalue(name)
            break
    if page is not None:
        save_failure_screenshot(page, request.node.nodeid)
