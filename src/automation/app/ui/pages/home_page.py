from __future__ import annotations
from automation.app.ui.components.search_component import SearchComponent
from automation.core.ui import BasePage
from playwright.sync_api import Locator
from playwright.sync_api import Page


class HomePage(BasePage):
    @property
    def search_component(self) -> SearchComponent:
        return SearchComponent(self.page)

    # @property
    # def search_input(self) -> Locator:
    #     return self.page.locator("#twotabsearchtextbox")

    # @property
    # def search_button(self) -> Locator:
    #     return self.page.locator("#nav-search-submit-button")

    # def search_item(self, text: str) -> None:
    #     self.fill(self.search_input, text)
    #     self.click(self.search_button)
