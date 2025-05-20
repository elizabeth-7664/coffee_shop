# coffee.py
from order import Order

class Coffee:
    all_coffees = []

    def __init__(self, name):
        self.name = name  # will call setter with validation
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")

    def orders(self):
        """Return a list of all orders for this coffee."""
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        """Return a unique list of customers who ordered this coffee."""
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        """Return total number of times this coffee has been ordered."""
        return len(self.orders())

    def average_price(self):
        """Return the average price paid for this coffee."""
        orders = self.orders()
        if orders:
            return sum(order.price for order in orders) / len(orders)
        return 0
