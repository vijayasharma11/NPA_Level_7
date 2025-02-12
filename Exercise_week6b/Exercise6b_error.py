import json
import os
import sys
location = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(location)
# The above four lines changes the directory to the location of your python code
and files.
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
def update_quantity(inventory):
name = input("Enter product name: ")
for product in inventory:
if product["name"] == name:
new_quantity = int(input("Enter new quantity: "))
product["quantity"] = new_quantity
print("Quantity updated successfully!")
return
print("Product not found.")
def display_inventory(inventory):
print("Current Inventory:")
for product in inventory:
print(f"- {product['name']} ({product['category']}):
{product['quantity']}")
def main():
inventory = load_inventory()
while True:
print("\nWelcome to the Inventory Management System!\n")
print("1. Add a new product")
print("2. Update product quantity")
print("3. Display current inventory")
print("4. Save inventory to JSON file")
print("5. Exit\n")
choice = input("Enter your choice: ")
if choice == "1":
add_product(inventory)
elif choice == "2":
update_quantity(inventory)
elif choice == "3":
display_inventory(inventory)
elif choice == "4":
save_inventory(inventory)
print("Inventory saved to 'inventory.json'.")
elif choice == "5":
print("Exiting program. Goodbye!")
break
else:
print("Invalid choice. Please try again.")
if __name__ == "__main__":
main()