class Product():
    
    def __init__(self, product_id: int, name, price: float, stock_quantity: int):
        self._product_id = product_id #int
        self._name = name
        self._price = price #float
        self._stock_quantity = stock_quantity #int

    def get_product_id(self):
        return self._product_id

    def update_price(self, new_price):
        self._price = new_price

    def update_stock(self, quantity):
        self._stock_quantity = quantity

    def is_in_stock(self, quantity):
        return True if self._stock_quantity > quantity else False
    
    def sell(self, quantity):
        
        if quantity <= 0:
            raise Exception('Sale Canceled: quantity must be positive')
        elif quantity > self._stock_quantity:
            raise Exception(f"{quantity} is a lot!, we only have {self._stock_quantity}")
        elif quantity <= self._stock_quantity:
            self._stock_quantity -= quantity

        return quantity * self._price
    
    #Added these two methods to complete the Test Cases
    def get_product_details(self):
        return f"{self._name}, Price: {self._price}, Quantity: {self._stock_quantity}"
    
    def get_stock_quantity(self):
        return self._stock_quantity
    

#Eelctronic Products
class ElectronicsProduct(Product):
    def __init__(self, product_id: int, name, price: int, stock_quantity: int, warranty_period: int):
        super().__init__(product_id, name, price, stock_quantity)
        self._warranty_period = warranty_period
    
    def get_product_details(self):
        return f"{self._name}, Price: {self._price}, Quantity: {self._stock_quantity}, Warranty Remaining (Months): {self._warranty_period}"


#Perishable Products Class
class PerishableProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, expiration_date):
        super().__init__(product_id, name, price, stock_quantity)
        self._expiration_date = expiration_date
    
    def get_product_details(self):
        return f"{self._name}, Price: {self._price}, Quantity: {self._stock_quantity}, Expiration Date: {self._expiration_date}"

