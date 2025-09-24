from product import *

class Inventory():
    inventory = {}

    def __init__(self, product):
        self.product = product

    def add_product(self, product):
        Inventory.inventory.update({product.get_product_id(): product})

    def remove_product(self, product_id):
        del Inventory.inventory[product_id]
    
    def list_products():
        for product in Inventory.inventory:
            product.get_product_details()