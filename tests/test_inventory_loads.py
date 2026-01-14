from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_page_loads_after_login():
    with sync_playwright() as p:
        def test_inventory_loads(page):
            login_page = LoginPage(page)
            login_page.navigate()
            login_page.login("standard_user", "secret_sauce")
            