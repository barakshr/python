"""App-agnostic Playwright component wrapper. Product widgets belong in app/ui/components."""

from __future__ import annotations
from playwright.sync_api import Locator
from automation.core.ui.base_actions import BaseActions


class BaseComponent(BaseActions):
    pass
