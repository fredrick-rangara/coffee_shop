from customer import Customer
from coffee import Coffee
from order import Order

print("--- Starting Debug ---")

# 1. Create Instances
cust1 = Customer("Steve")
cust2 = Customer("Dianna")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

print(f"Created Customer: {cust1.name}")
print(f"Created Coffee: {coffee1.name}")

# 2. Create Orders
# Steve buys 2 Lattes and 1 Espresso
cust1.create_order(coffee1, 5.00)
cust1.create_order(coffee1, 5.00)
cust1.create_order(coffee2, 3.00)

# Dianna buys 1 Latte (expensive one)
cust2.create_order(coffee1, 9.0)

print(f"Total Global Orders: {len(Order.all)}")

# 3. Test Relationships
print(f"\n--- Testing Relationships ---")
print(f"Steve's Order count: {len(cust1.orders())} (Expected: 3)")
print(f"Latte's Order count: {coffee1.num_orders()} (Expected: 3)")
print(f"Latte's Average Price: {coffee1.average_price()} (Expected: 6.33 approx)")
print(f"Dianna's Order count: {len(cust2.orders())} (Expected: 1)")
print(f"Dianna's Total Spend: ${sum([o.price for o in cust2.orders()])}")

# 4. Test Aggregation (Most Aficionado)
# Steve spent $10 on Latte. Dianna spent $9 on Latte.
# Steve should be the aficionado.
aficionado = Customer.most_aficionado(coffee1)
print(f"\n--- Testing Logic ---")
print(f"Who loves Lattes most? {aficionado.name} (Expected: Steve)")

# 5. Test Validations (Uncomment to test exceptions)
# try:
#     Customer("ThisNameIsWayTooLongForTheValidation")
# except ValueError as e:
#     print(f"Validation Caught: {e}")

print("\n--- End Debug ---")