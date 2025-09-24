from product import *

class Inventory():
    inventory = {}

    def add_product(self, product):
        Inventory.inventory.update({product.get_product_id(): product})

    def remove_product(self, product_id):
        del Inventory.inventory[product_id]
    
    def list_products(self):
        for product in Inventory.inventory.values():
            return product.get_product_details()