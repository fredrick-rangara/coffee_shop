class Order:
    #Single source of truth
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not (1.00 <= value <= 10.00):
            raise ValueError("Price must be between 1.00 and 10.00")
        self._price = value
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self,value):
        #We check the class name to avoid circular imports
        if type(value).__name__ != "Customer":
            raise TypeError("Must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if type(value).__name__ != "Coffee":
            raise TypeError("Must be a Coffee instance")
        self._coffee = value
        