import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username,password,expected_result",

    [
        ("standard_user", "secret_sauce", "success"),
        ("locked_out_user", "secret_sauce", "locked"),
        ("invalid_user", "wrong_password", "invalid"),
    ],
)
def test_login_variants(page, username, password, expected_result):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    if expected_result == "success":
        assert "inventory" in page.url

    elif expected_result == "locked":
        assert "locked out" in login_page.get_error_message().lower()

    elif expected_result == "invalid":
        assert "username and password do not match" in login_page.get_error_message().lower()