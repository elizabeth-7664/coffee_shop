import pytest
from coffee import Coffee
from order import Order
from customer import Customer

# Clear class-level lists before each test (to avoid test pollution)
@pytest.fixture(autouse=True)
def clear_data():
    Coffee.all_coffees.clear()
    Order.all_orders.clear()
    yield
    Coffee.all_coffees.clear()
    Order.all_orders.clear()

def test_coffee_name_valid():
    c = Coffee("Latte")
    assert c.name == "Latte"

def test_coffee_name_invalid():
    with pytest.raises(ValueError):
        Coffee("ab")  # less than 3 chars

def test_orders_and_customers():
    c1 = Coffee("Espresso")
    cust1 = Customer("Alice")
    cust2 = Customer("Bob")

    # Create orders manually (without create_order method)
    o1 = Order(cust1, c1, 3.5)
    o2 = Order(cust2, c1, 4.0)
    o3 = Order(cust1, c1, 4.5)

    # Orders list
    orders = c1.orders()
    assert len(orders) == 3
    assert o1 in orders and o2 in orders and o3 in orders

    # Customers list (unique)
    customers = c1.customers()
    assert len(customers) == 2
    assert cust1 in customers and cust2 in customers

def test_num_orders_and_average_price():
    c1 = Coffee("Cappuccino")
    cust = Customer("Eve")
    Order(cust, c1, 2.0)
    Order(cust, c1, 4.0)
    Order(cust, c1, 6.0)

    assert c1.num_orders() == 3
    assert c1.average_price() == pytest.approx(4.0)

def test_average_price_no_orders():
    c = Coffee("Mocha")
    assert c.average_price() == 0
