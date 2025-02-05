# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 21/01/2025
# Purpose: creating a simple inventory management system to keep track of products in a store. 
# #The system should allow users to perform various operations such as adding new products, 
# #updating product quantities, and displaying the current inventory.

#-----------------------------------------------------------------

import json
import os

# File to store the inventory data
INVENTORY_FILE = "inventory.json"

# Load existing inventory data from the JSON file
def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# Save the current inventory data to the JSON file
def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(inventory, file, indent=4)

# Add a new product to the inventory
def add_product(inventory):
    product_name = input("Enter the product name: ").strip()
    category = input("Enter the product category: ").strip()
    try:
        quantity = int(input("Enter the product quantity: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return
    
    # Add the product to the inventory
    inventory[product_name] = {
        "category": category,
        "quantity": quantity
    }
    print(f"Product '{product_name}' added successfully.")

# Update the quantity of an existing product
def update_quantity(inventory):
    product_name = input("Enter the product name: ").strip()
    
    if product_name in inventory:
        try:
            quantity = int(input("Enter the new quantity: "))
            inventory[product_name]["quantity"] = quantity
            print(f"Quantity for '{product_name}' updated to {quantity}.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print(f"Product '{product_name}' not found in inventory.")

# Display the current inventory
def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return

    print(f"{'Product Name':<20} {'Category':<20} {'Quantity':<10}")
    print("-" * 50)
    
    for product, details in inventory.items():
        print(f"{product:<20} {details['category']:<20} {details['quantity']:<10}")

# Main function to display the menu and handle user input
def main():
    inventory = load_inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add a new product")
        print("2. Update product quantity")
        print("3. Display current inventory")
        print("4. Save inventory to JSON file")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            update_quantity(inventory)
        elif choice == '3':
            display_inventory(inventory)
        elif choice == '4':
            save_inventory(inventory)
            print("Inventory saved to 'inventory.json'.")
        elif choice == '5':
            save_inventory(inventory)
            print("Exiting program and saving inventory.")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")

# Entry point for the program
if __name__ == "__main__":
    main()



'''
OUTPUT:

d:/Vijaya/NPA_Level_7/Challenge_3B_inventory_management_system/Inventory_management_system.py

Inventory Management System
1. Add a new product
2. Update product quantity
3. Display current inventory
4. Save inventory to JSON file
5. Exit

Choose an option (1-5): 1
Enter the product name: Apple
Enter the product category: fruits
Enter the product quantity: 56
Product 'Apple' added successfully.

Inventory Management System
1. Add a new product
2. Update product quantity
3. Display current inventory
4. Save inventory to JSON file
5. Exit

Choose an option (1-5): 2
Enter the product name: Apple
Enter the new quantity: 76
Quantity for 'Apple' updated to 76.

Inventory Management System
1. Add a new product
2. Update product quantity
3. Display current inventory
4. Save inventory to JSON file
5. Exit

Choose an option (1-5): 3
Product Name         Category             Quantity
--------------------------------------------------
Apple                fruits               76

Inventory Management System
1. Add a new product
2. Update product quantity
3. Display current inventory
4. Save inventory to JSON file
5. Exit

Choose an option (1-5): 4
Inventory saved to 'inventory.json'.

Inventory Management System
1. Add a new product
2. Update product quantity
3. Display current inventory
4. Save inventory to JSON file
5. Exit

Choose an option (1-5): 5
Exiting program and saving inventory.

'''