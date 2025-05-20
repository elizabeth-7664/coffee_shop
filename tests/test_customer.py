# tests/test_customer.py
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    Customer.all_customers.clear()
    Coffee.all_coffees.clear()
    Order.all_orders.clear()

def test_valid_customer_name():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_invalid_customer_name_too_long():
    with pytest.raises(ValueError):
        Customer("A very very long name")

def test_invalid_customer_name_empty():
    with pytest.raises(ValueError):
        Customer("")

def test_orders_and_coffees():
    c = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    o1 = c.create_order(coffee1, 5.0)
    o2 = c.create_order(coffee2, 7.0)
    o3 = c.create_order(coffee1, 4.0)

    assert len(c.orders()) == 3
    assert set(c.coffees()) == {coffee1, coffee2}

def test_most_aficionado():
    c1 = Customer("John")
    c2 = Customer("Jane")
    coffee = Coffee("Cappuccino")

    c1.create_order(coffee, 4.0)
    c1.create_order(coffee, 6.0)
    c2.create_order(coffee, 8.0)

    assert Customer.most_aficionado(coffee) == c1  # 10.0 > 8.0

    c2.create_order(coffee, 3.0)  # Now c2 = 11.0
    assert Customer.most_aficionado(coffee) == c2
