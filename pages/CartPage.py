from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page

        # Confirms the user is on the cart page
        self.cart_title = page.get_by_text("Your Cart")
        self.checkout_cart_button = page.get_by_role('button', name="Checkout")

    def confirm_cart_items(self):
        expect(self.cart_title).to_be_visible()

        self.checkout_cart_button.click()