class Product():
    
    def __init__(self, product_id, name, price, stock_quantity):
        self.__product_id = product_id #int
        self.__name = name
        self.__price = price #float
        self.__stock_quantity = stock_quantity #int

    def update_price(self, new_price):
        self.__price = new_price

    def update_stock(self, quantity):
        self.__stock_quantity = quantity

    def is_in_stock(self, quantity):
        return True if self.__stock_quantity > quantity else False
    
    def sell(self, quantity):
        if quantity > self.__stock_quantity:
            raise Exception(f"{quantity} is a lot!, we only have {self.__stock_quantity}")
        elif quantity <= self.__stock_quantity:
            self.__stock_quantity -= quantity

        return quantity * self.__price
    
    def get_product_details(self):
        return f"{self.__name}, Price: {self.__price}, Quantity: {self.__stock_quantity}"
    

#Eelctronic Products
class ElectronicsProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, warranty_period):
        super().__init__(product_id, name, price, stock_quantity)
        self.__warranty_period = warranty_period
    
    def get_product_details(self):
        return f"{self.__name}, Price: {self.__price}, Quantity: {self.__stock_quantity}, Warranty Remaining (Months): {self.__warranty_period}"


#Perishable Products Class
class PerishableProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, expiration_date):
        super().__init__(product_id, name, price, stock_quantity)
        self.__expiration_date = expiration_date
    
    def get_product_details(self):
        return f"{self.__name}, Price: {self.__price}, Quantity: {self.__stock_quantity}, Expiration Date: {self.__expiration_date}"

