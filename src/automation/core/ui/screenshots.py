"""UI screenshot helpers (app-agnostic)."""

from pathlib import Path

from playwright.sync_api import Page

ARTIFACTS = Path("artifacts/screenshots")


def save_failure_screenshot(page: Page, test_nodeid: str) -> Path:
    """Capture a full-page screenshot for a failed test under ``artifacts/screenshots``."""
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    safe_name = test_nodeid.replace("/", "_").replace("::", "_")
    path = ARTIFACTS / f"{safe_name}.png"
    page.screenshot(path=str(path), full_page=True)
    return path
