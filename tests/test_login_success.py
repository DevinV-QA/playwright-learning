from playwright.sync_api import sync_playwright, expect

def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open login page
        page.goto("https://www.saucedemo.com/")

        # Enter credentials
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")

        # Click login
        page.locator("[data-test='login-button']").click()

        # Assert inventory page loaded
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

        # Optional: check a product is visible
        expect(page.locator(".inventory_item")).to_have_count(6)

        browser.close()
    