class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        # Returns unique list of coffees
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order
        # This creates the order and automatically appends it to Order.all
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        
        # Get all orders for this specific coffee
        coffee_orders = [o for o in Order.all if o.coffee == coffee]
        
        if not coffee_orders:
            return None

        # Map customers to their total spend on this coffee
        spending_map = {}
        
        for order in coffee_orders:
            if order.customer not in spending_map:
                spending_map[order.customer] = 0
            spending_map[order.customer] += order.price

        # Find the customer with the highest spending
        # max() with a key argument finds the key with the highest value
        highest_spender = max(spending_map, key=spending_map.get)
        
        return highest_spender