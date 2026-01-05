from playwright.sync_api import sync_playwright, expect

def test_login_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        expect(page.locator("[data-test='login-button']")).to_be_visible()

        browser.close()
    