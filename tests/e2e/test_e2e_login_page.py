import re

from faker import Faker
from playwright.sync_api import expect

from pages.LoginPage import LoginPage

fake = Faker("pt_BR")

username_fake = fake.user_name()
pwd_fake = fake.password()


def test_login_valid(page):
    """
    GIVEN the user is on the login page
    WHEN the user logs in with valid credentials
    AND clicks the Login button
    THEN the products page should be displayed
    """
    login = LoginPage(page)

    login.visit()
    login.login_access("standard_user", "secret_sauce")

    expect(page).to_have_url(re.compile("/inventory"))


def test_login_invalid_credentials(page):
    """
    GIVEN the user is on the login page
    WHEN the user logs in with invalid credentials
    AND clicks the Login button
    THEN the error message "Username and password do not match any user" should be displayed
    AND the user should remain on the login page
    """
    login = LoginPage(page)

    login.visit()
    login.login_access(username_fake, pwd_fake)

    expect(login.error_user_pwd_invalid).to_be_visible()


def test_login_empty_username(page):
    """
    GIVEN the user is on the login page
    WHEN the user tries to log in with the username field empty
    AND clicks the Login button
    THEN the error message "Username is required" should be displayed
    AND the user should remain on the login page
    """
    login = LoginPage(page)

    login.visit()
    login.login_access("", pwd_fake)

    expect(login.error_username_required).to_be_visible()


def test_login_empty_pwd(page):
    """
    GIVEN the user is on the login page
    WHEN the user tries to log in with the password field empty
    AND clicks the Login button
    THEN the error message "Password is required" should be displayed
    AND the user should remain on the login page
    """
    login = LoginPage(page)

    login.visit()
    login.login_access(username_fake, "")

    expect(login.error_pwd_required).to_be_visible()
