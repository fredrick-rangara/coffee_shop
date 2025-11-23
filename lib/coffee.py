# We use a local import inside methods to avoid circular dependency errors
# caused by Order importing Coffee and Coffee importing Order.

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 chracters long")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        # Returns a unique list of customners
        return list ({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total_price = sum([order.price for order in orders])
        return total_price / len(orders)