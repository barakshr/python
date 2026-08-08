from __future__ import annotations
from automation.app.ui.components.search_component import SearchComponent
from automation.app.ui.components.top_bar_component import TopBarComponent
from automation.core.ui import BasePage
from playwright.sync_api import Locator
from playwright.sync_api import Page


class HomePage(BasePage):
    @property
    def top_bar_component(self) -> TopBarComponent:
        return TopBarComponent(self.page)
