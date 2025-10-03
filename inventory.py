from product import *

class Inventory():

    def __init__(self, name):
        self._name = name
        self._inventory = {}

    # storing product as value to its id as a key
    def add_product(self, product):
        self._inventory.update({product.get_product_id(): product})

    def remove_product(self, product_id):
        del self._inventory[product_id]
    
    def list_products(self):
        list = []
        for product in self._inventory.values(): #Iterating over values not keys
            list.append(product.get_product_details())

        return list #returns a list