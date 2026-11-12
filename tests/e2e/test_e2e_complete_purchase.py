from faker import Faker

from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.ProductsPage import ProductsPage

fake = Faker("pt_BR")

fake_first_name = fake.first_name()
fake_last_name = fake.last_name()
fake_zip_code = fake.numerify("#####-###")


def test_complete_purchase(logged_page):
    """
    GIVEN the user is logged in
    AND has added products to the cart
    WHEN the user completes the checkout
    THEN the order confirmation message should be displayed
    """
    products = ProductsPage(logged_page)
    cart = CartPage(logged_page)
    checkout = CheckoutPage(logged_page)

    products.select_products_to_cart()
    cart.confirm_cart_items()
    checkout.complete_checkout(fake_first_name, fake_last_name, fake_zip_code)
