from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

        # Add items to the cart
        self.add_cart_backpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.add_cart_jacket = page.locator("#add-to-cart-sauce-labs-fleece-jacket")

        # Open the cart
        self.cart_button = page.locator(".shopping_cart_link")

    def select_products_to_cart(self):
        self.add_cart_backpack.click()
        self.add_cart_jacket.click()

        self.cart_button.click()

