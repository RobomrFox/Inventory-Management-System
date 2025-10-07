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


#Edge cases List
zero_qty_cases = [
    (1, 0),          
    (2, 0),
]

overstock_cases = [
    (1, 9999),       
    (3, 1000),
]

nonexistent_cases = [
    (12345, 5),      
    (99999, 1),
]

#This test does Adding, Selling and Listing Products
def Test(adding_test): 
    print("\033[35m Starting Tests\n\033[0m") #Purple color print statement

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
    print('\n'.join(inventory.list_products())) # instead of a list it joins every item with a new line '\n' and print the next element on the next line :)
    print('\n')

    #selling test
    for pos_sale in selling_list: 
        item = pos_sale[0]
        qty = pos_sale[1]

        sale = Sale(item, qty).process_sale()

    print('After Sales')
    print('\n'.join(inventory.list_products()))

    return inventory


def Edge_Case_Test(inv, zero_cases, over_cases, nonexistent_cases):
    print('\033[95m\n Edge cases start, jst writing this line for space \n\033[0m')

    #when selling qty is 0
    for id, qty in zero_cases:
        print(f'Zero Qunatity Test: product id {id} and qty: {qty}')
        prod = inv.get_product(id)

        if prod is None:
            print("Product not found")
            continue

        original_qty = prod.get_stock_quantity()

        #revenue is 0 for no sale
        revenue = Sale(prod, qty).process_sale()

        if revenue == 0 and original_qty == prod.get_stock_quantity():
            print('Test Passed, nothing sold for 0 qty')
        else: 
            print('Test failed')

    print('\n')

    #overstock cases
    for id, qty in over_cases:
        print(f'Overstock Test: product id {id} and qty: {qty}')
        prod = inv.get_product(id)

        if prod is None:
            print("Product not found")
            continue

        original_qty = prod.get_stock_quantity()

        #revenue is 0 for no sale
        revenue = Sale(prod, qty).process_sale()

        if revenue == 0 and original_qty == prod.get_stock_quantity():
            print('Test Passed, no sale for overstock qty')
        else: 
            print('Test failed')

    print('\n')

    for id, qty in nonexistent_cases:
        print(f'Not existence Test: product id {id} and qty: {qty}')
        prod = inv.get_product(id)

        if prod is None:
            print(f'Test Passed! Product {id} not found.')
        else:
            print('Test Failed: product exists')