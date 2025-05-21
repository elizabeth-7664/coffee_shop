# ☕ Coffee Shop Ordering System

A simple Python application for managing coffee orders, built using OOP principles. It features three main classes: `Customer`, `Coffee`, and `Order`.

---

## 📁 Project Structure

coffe_shop/
├── coffee.py
├── customer.py
├── order.py
├── tests/
│ ├── init.py
│ └── test_customer.py
│ └── test_coffee.py
├── venv/ (optional virtual environment)
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

1. **Clone the repository** (or navigate to your project directory).
2. **Set up a virtual environment** (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

    Install dependencies:

pip install -r requirements.txt

Run tests:

    python3 -m pytest

🧠 Class Features
Customer

    Stores all instances in Customer.all_customers

    Validates name: string between 1 and 15 characters

    Methods:

        orders()

        coffees()

        create_order(coffee, price)

        most_aficionado(coffee) (class method)

Coffee

    Stores all instances in Coffee.all_coffees

    Validates name: string with at least 3 characters

    Methods:

        orders()

        customers()

        num_orders()

        average_price()

Order

    Stores all orders in Order.all_orders

    Validates:

        customer must be a Customer instance

        coffee must be a Coffee instance

        price must be a float between 1.0 and 10.0

✅ Testing

    Uses pytest

    All test files are located in the tests/ directory

    To run tests:

    python3 -m pytest

📦 requirements.txt

pytest==4.6.9

    This version is compatible with Python 2.7 if you're working in a legacy environment.

