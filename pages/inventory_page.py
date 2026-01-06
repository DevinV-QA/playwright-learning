from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = Page

        # Locators
        self.inventory_container = page.locator(".inventory_list")
        self.cart_badge = page.locator(".shopping_cart_badge")

        # Example item (Sauce Labs Backpack)
        self.add_backpack_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.remove_backpack_button = page.locator ("[data-test='remove-sauce-labs-backpack']")
        self.cart_link = page.locator(".shopping_cart_link")

    def is_loaded(self):
        return self.inventory_container.is_visible()
    
    def add_backpack_to_cart(self):
        self.add_backpack_button.click()

    def remove_backpack_from_cart(self):
        self.remove_backpack_button.click()

    def get_cart_count(self):
        return self.cart_badge.text_content()
    
    def go_to_cart(self):
        self.cart_link.click()