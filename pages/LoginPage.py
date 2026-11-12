from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        # Login fields
        self.page = page
        self.username_input = page.locator('#user-name')
        self.pwd_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")

        # Error messages
        self.error_username_required = page.locator(".error", has_text="Username is required")
        self.error_pwd_required = page.locator(".error", has_text="Password is required")
        self.error_user_pwd_invalid = page.locator(".error", has_text="Username and password do not match any user")

    def visit(self):
        self.page.goto("https://www.saucedemo.com/")

    def login_access(self, username, pwd):

        self.username_input.fill(username)
        self.pwd_input.fill(pwd)
        self.login_button.click()

