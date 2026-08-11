"""Shared fixtures for all tests (config, logging, etc.)."""

import pytest

from automation.core.config import Settings

# Must live in a top-level conftest (pytest 8+); non-top-level breaks discovery.
pytest_plugins = ["automation.core.ui.pytest_plugin"]


@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings(base_url="")
