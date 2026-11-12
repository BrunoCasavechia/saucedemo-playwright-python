import pytest
from pages.LoginPage import LoginPage

@pytest.fixture
def logged_page(page):
    login = LoginPage(page)
    login.visit()
    login.login_access("standard_user", "secret_sauce")
    return page