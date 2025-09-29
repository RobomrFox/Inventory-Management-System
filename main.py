from product import *
from inventory import *

def main():
    print("Hello from inventory-management-system!")

    milk = Product(1234, 'Milk', 23.49, 50)

    eggs = Product(2232, 'Eggs', 10.99, 10)

    print(milk.get_product_details())

    inventory = Inventory('Groceries')
    inventory.add_product(eggs)

    print(inventory.list_products())


if __name__ == "__main__":
    main()
