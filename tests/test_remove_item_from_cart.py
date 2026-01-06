from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_remove_item_updates_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_backpack_to_cart()
        inventory_page.remove_backpack_from_cart()

        expect(inventory_page.cart_badge).not_to_be_visible()

        browser.close()