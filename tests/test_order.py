# tests/test_order.py
import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def setup_function():
    Order.all_orders.clear()
    Customer.all_customers.clear()
    Coffee.all_coffees.clear()

def test_valid_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    assert order in Order.all_orders

def test_invalid_customer():
    coffee = Coffee("Latte")
    with pytest.raises(TypeError):
        Order("NotACustomer", coffee, 5.0)

def test_invalid_coffee():
    customer = Customer("Alice")
    with pytest.raises(TypeError):
        Order(customer, "NotACoffee", 5.0)

def test_invalid_price_type():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, 12.0)

def test_invalid_price_not_float():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, 5)  # int instead of float
