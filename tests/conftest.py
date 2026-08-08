"""Shared fixtures for all tests (config, logging, etc.)."""

import pytest

from automation.core.config import Settings


@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings(base_url="")
