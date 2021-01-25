class Product:
    def __init__(self, price):
        self.price = price

    # auto magically create a property called price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
   
    # property for setting / getting
    # price = property(get_price, set_price)
    
product = Product(30)
print(product.price)
