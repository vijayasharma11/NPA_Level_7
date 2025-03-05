# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 15/01/2025
# Purpose: Debug the provided Python code to fix errors using breakpoints.
#-----------------------------------------------------------------
import json
import os
import sys

# Set working directory to script location
location = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(location)

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
    except FileNotFoundError:
        inventory = []
    return inventory

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

def add_product(inventory):
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    quantity = int(input("Enter product quantity: "))
    product = {"name": name, "category": category, "quantity": quantity}
    inventory.append(product)
    print("Product added successfully!")
    save_inventory(inventory)  # Save after adding

def update_quantity(inventory):
    name = input("Enter product name: ")
    for product in inventory:
        if product["name"].lower() == name.lower():
            new_quantity = int(input("Enter new quantity: "))
            product["quantity"] = new_quantity
            print("Quantity updated successfully!")
            save_inventory(inventory)  # Save after updating
            return
    print("Product not found.")

def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for product in inventory:
        print(f"- {product['name']} ({product['category']}): {product['quantity']}")

def main():
    inventory = load_inventory()
    
    while True:
        print("\nWelcome to the Inventory Management System!\n")
        print("1. Add a new product")
        print("2. Update product quantity")
        print("3. Display current inventory")
        print("4. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            update_quantity(inventory)
        elif choice == "3":
            display_inventory(inventory)
        elif choice == "4":
            save_inventory(inventory)
            print("Inventory saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


'''
Welcome to the Inventory Management System!

1. Add a new product
2. Update product quantity
3. Display current inventory
4. Exit

Enter your choice: 1
Enter product name: Apple
Enter product category: Fruits
Enter product quantity: 45
Product added successfully!

Welcome to the Inventory Management System!

1. Add a new product
2. Update product quantity
3. Display current inventory
4. Exit

Enter your choice: 2
Enter product name: Apple
Enter new quantity: 56
Quantity updated successfully!

Welcome to the Inventory Management System!

1. Add a new product
2. Update product quantity
3. Display current inventory
4. Exit

Enter your choice: 3

Current Inventory:
- Apple (Fruits): 56

Welcome to the Inventory Management System!

1. Add a new product
2. Update product quantity
3. Display current inventory
4. Exit

Enter your choice: 4
Inventory saved. Exiting...

'''