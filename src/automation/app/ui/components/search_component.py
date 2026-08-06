from playwright.sync_api import Locator
from playwright.sync_api import Page

from automation.core.ui.base_actions import BaseActions


class SearchComponent(BaseActions):
    def __init__(self, page: Page):
        self.page = page

    @property
    def search_input(self) -> Locator:
        return self.page.locator("#twotabsearchtextbox")

    @property
    def search_button(self) -> Locator:
        return self.page.locator("#nav-search-submit-button")

    def search_item(self, text: str) -> None:
        self.fill(self.search_input, text)
        self.click(self.search_button)
