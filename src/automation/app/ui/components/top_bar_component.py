from playwright.sync_api import Locator
from playwright.sync_api import Page

from automation.app.ui.pages.cart_page import CartPage
from automation.app.ui.pages.producs_page import ProductsPage
from automation.core.ui.base_actions import BaseActions
from automation.core.config.settings import get_settings


class TopBarComponent(BaseActions):
    def __init__(self, page: Page):
        self.page = page

    @property
    def product_link(self) -> Locator:
        return self.page.get_by_role("link", name="Products")

    @property
    def cart_link(self) -> Locator:
        return self.page.get_by_role("link", name="Cart")

    def goto_products(self, via_link: bool = False) -> ProductsPage:
        if via_link:
            self.click(self.product_link)
        else:
            self.page.goto(f"{get_settings().base_url}/products")
        return ProductsPage(self.page)

    def goto_cart(self) -> CartPage:
        return CartPage(self.page)
