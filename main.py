from product import *
from inventory import *
from test_main import *

def main():
    print("Hello from inventory-management-system!")
    print('\n')

    inv = Test(adding_products_test) # Test returns the inventory for the next test Edge Case

    Edge_Case_Test(inv, zero_qty_cases,  overstock_cases, nonexistent_cases)


if __name__ == "__main__":
    main()
