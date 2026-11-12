from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):

        self.page = page

        # Confirms the user is on the checkout page
        self.checkout_title = page.get_by_text("Checkout: Your Information")
        
        # Form fields
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.zip_code_input = page.get_by_placeholder("Zip/Postal Code")

        # Confirm form button
        self.confirm_form_button = page.get_by_role("button", name="Continue")

        # Finish order button
        self.finish_order_button = page.get_by_role("button", name="Finish")

        # Order confirmation message
        self.validate_order_text = page.get_by_role("heading", name="Thank you for your order!")

    def complete_checkout(self, first_name, last_name, zip_code):

        # Confirms the user is on the checkout page
        expect(self.checkout_title).to_be_visible()

        # Fill in the form fields
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_code_input.fill(zip_code)

        # Finish the order
        self.confirm_form_button.click()
        self.finish_order_button.click()

        # Order confirmation message is visible
        expect(self.validate_order_text).to_be_visible()
        