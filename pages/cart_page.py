from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.cart_items = page.locator(".cart_item")
    
    def get_item_count(self):
        return self.cart_items.count()