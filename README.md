# SauceDemo – E2E Test Automation

End-to-end test automation for [SauceDemo](https://www.saucedemo.com/), built with **Python**, **Playwright** and **Pytest** using the **Page Object Model (POM)** design pattern.

## Tech Stack

- [Python 3](https://www.python.org/)
- [Playwright](https://playwright.dev/python/) – browser automation
- [Pytest](https://docs.pytest.org/) + [pytest-playwright](https://github.com/microsoft/playwright-pytest) – test runner and fixtures
- [pytest-html](https://pytest-html.readthedocs.io/) – HTML test report
- [Faker](https://faker.readthedocs.io/) – dynamic test data generation

## Project Structure

```
Project-SauceDemo/
├── pages/                      # Page Objects
│   ├── LoginPage.py
│   ├── ProductsPage.py
│   ├── CartPage.py
│   └── CheckoutPage.py
├── tests/
│   ├── conftest.py             # Shared fixtures (e.g. logged_page)
│   └── e2e/
│       ├── test_e2e_login_page.py
│       └── test_e2e_complete_purchase.py
├── pytest.ini
└── requirements.txt
```

## Test Scenarios

Test cases are documented using the **Given / When / Then** (BDD) format.

### Login
| Scenario | Expected result |
|---|---|
| Login with valid credentials | User is redirected to the products page |
| Login with invalid credentials | Error: *"Username and password do not match any user"* |
| Login with empty username | Error: *"Username is required"* |
| Login with empty password | Error: *"Password is required"* |

### Complete Purchase
| Scenario | Expected result |
|---|---|
| Add products to the cart, fill in the checkout form and finish the order | Message *"Thank you for your order!"* is displayed |

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/<your-username>/Project-SauceDemo.git
cd Project-SauceDemo

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
playwright install
```

### Running the tests

```bash
# Run all tests (headless)
pytest

# Run with the browser visible
pytest --headed

# Run a specific test file
pytest tests/e2e/test_e2e_login_page.py

# Run on a different browser
pytest --browser firefox
```

## Test Report

An HTML report is generated automatically after each run at `report.html` (configured in `pytest.ini`).

## Author

**Bruno Casavechia**
