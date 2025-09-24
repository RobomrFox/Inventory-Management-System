from product import *

class Sale():
    def __init__(self, product, selling_quantity):
        self.__product = product
        self.__selling_quantity = selling_quantity

    def process_sale(self):
        try:
            self.__product.sell(self.__selling_quantity)

        #Exception from Product class sell()
        except Exception as e:
            print(e)
            return 0