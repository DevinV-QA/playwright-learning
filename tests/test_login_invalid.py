from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage

def test_invalid_login_shows_error():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("wrong_user", "wrong_password")

        expect(login_page.error_message).to_be_visible()

        browser.close()