# debug.py
from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Ali")
c2 = Customer("Brenda")
c3 = Customer("Charles")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# Creating orders
c1.create_order(coffee1, 3.5)
c1.create_order(coffee1, 4.0)
c2.create_order(coffee1, 5.0)
c3.create_order(coffee2, 2.5)

# Testing outputs
print(f"{c1.name} has ordered: {[c.name for c in c1.coffees()]}")
print(f"{coffee1.name} has been ordered {coffee1.num_orders()} times.")
print(f"Average price of {coffee1.name}: {coffee1.average_price():.2f}")
print(f"Top aficionado of {coffee1.name}: {Customer.most_aficionado(coffee1).name}")
