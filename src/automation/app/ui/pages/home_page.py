from __future__ import annotations
from automation.app.ui.components.search_component import SearchComponent
from automation.core.ui import BasePage
from playwright.sync_api import Locator
from playwright.sync_api import Page


class HomePage(BasePage):
    @property
    def search_component(self) -> SearchComponent:
        return SearchComponent(self.page)
