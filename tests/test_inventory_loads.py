from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_page_loads_after_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
        
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(inventory_page.inventory_container).to_be_visible()
        
        browser.close()