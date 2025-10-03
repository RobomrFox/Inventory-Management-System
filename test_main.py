from product import Product, PerishableProduct, ElectronicsProduct
from inventory import Inventory
from sale import Sale
import random


# tuple has Product Class-0, Id-1, Name-2, Price-3, Quantity-4, etc. 
adding_products_test = [
    (Product, 1, "Shampoo", 5.99, 50), 
    (PerishableProduct, 2, "Milk", 6.57, 10, '2025-9-6'),
    (ElectronicsProduct, 3, "Headphones", 129.99, 10, 12), 
    (PerishableProduct,  4,  "Strawberries", 4.99,    40,     "2025-07-01"),
    (ElectronicsProduct,  5,  "USB Charger",  19.95,   60,      24),
    (Product, 6, "Lunch Box", 25.49, 23)
]


edge_cases = [] 

def Test(adding_test): 
    inventory = Inventory('Testing Inventory')

    selling_list = []

    for product in adding_test:  
        #get the individual component as product[2] = product[0](product[1:]) will try to mutate immutable tuple
        cls = product[0]
        params = product[1:]

        #unpacking params list with * :)
        item = cls(*params)

        #Adding to the inventory
        inventory.add_product(item)

        #selling quantity
        rand_sale_qty = random.randint(0, 10)

        selling_list.append((item, rand_sale_qty))

    #List new inventory
    print('Inventory List: ')
    print(inventory.list_products())

    #selling test
    for pos_sale in selling_list: 
        item = pos_sale[0]
        qty = pos_sale[1]

        sale = Sale(item, qty).process_sale()

    print('After Sales')
    print(inventory.list_products())
