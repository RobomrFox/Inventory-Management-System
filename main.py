from product import *

def main():
    print("Hello from inventory-management-system!")

    milk = Product(1234, 'Milk', 23.49, 50)

    print(milk.get_product_details())


if __name__ == "__main__":
    main()
