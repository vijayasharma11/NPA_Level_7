# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 15/01/2025
# Purpose: you will work with a dictionary named phone_book to manage your contacts' phone numbers. 
# A dictionary is a data structure in Python that stores key-value pairs. 
# In this case, each contact's name will serve as the key,
# and their phone number will be the corresponding value.
#-----------------------------------------------------------------

#creating an empty phone book dictionary
phone_book = {}

#Add a new contact to the phone book 
def add_contact():
    name = input("Enter the name of the person: ")
    phone_number = input("Enter the phone number: ")
    phone_book[name] = phone_number
    print(f"Contact {name} added successfully.")

#Update the phone number of an existing contact 
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in phone_book:
        new_phone_number = input("Enter the new phone number: ")
        phone_book[name] = new_phone_number
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

#Remove a contact from the phone book
def remove_contact():
    name = input("Enter the name of the contact to remove: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} removed successfully.")
    else:
        print(f"Contact {name} not found.")

#Function to check if a contact exists
def check_contact():
    name = input("Enter the name to check: ")
    if name in phone_book:
        print(f"Contact {name} exists with phone number {phone_book[name]}.")
    else:
        print(f"Contact {name} not found.")
    
# Function to display all contacts
def display_contacts():
     if phone_book:
        print("All contacts:")
        for name, phone_number in phone_book.items():
            print(f"{name}: {phone_number}")
     else:
            print("No contacts available.")


# Function to count the number of contacts
def count_contacts():
    print(f"Total number of contacts: {len(phone_book)}")

# Main function to display the menu 
def main():
    while True:
        print("\nPhone Book Menu:")
        print("1. Add a New Contact")
        print("2. Update Contact Information")
        print("3. Remove a Contact")
        print("4. Check Contact Existence")
        print("5. Display All Contacts")
        print("6. Count Contacts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            update_contact()
        elif choice == '3':
            remove_contact()
        elif choice == '4':
            check_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            count_contacts()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()


"""Output:
    Phone Book Menu:
1. Add a New Contact
2. Update Contact Information
3. Remove a Contact
4. Check Contact Existence
5. Display All Contacts
6. Count Contacts
7. Exit

Enter your choice (1-7): 1
Enter the name of the person: Naisha
Enter the phone number: 9876564400

Contact Naisha added successfully.

Phone Book Menu:
1. Add a New Contact
2. Update Contact Information
3. Remove a Contact
4. Check Contact Existence
5. Display All Contacts
6. Count Contacts
7. Exit

Enter your choice (1-7): 1
Enter the name of the person: Tom
Enter the phone number: 8978675645

Contact Tom added successfully.

Phone Book Menu:
1. Add a New Contact
2. Update Contact Information
3. Remove a Contact
4. Check Contact Existence
5. Display All Contacts
6. Count Contacts
7. Exit

Enter your choice (1-7): 1
Enter the name of the person: Ivy
Enter the phone number: 6789564534

Contact Ivy added successfully.

Phone Book Menu:
1. Add a New Contact
2. Update Contact Information
3. Remove a Contact
4. Check Contact Existence
5. Display All Contacts
6. Count Contacts
7. Exit

Enter your choice (1-7): 1
Enter the name of the person: Max
Enter the phone number: 9756452312

Contact Max added successfully.

Phone Book Menu:
1. Add a New Contact
2. Update Contact Information
3. Remove a Contact
4. Check Contact Existence
5. Display All Contacts
6. Count Contacts
7. Exit

Enter your choice (1-7): 2
Enter the name of the contact to update: Naisha
Enter the new phone number: 89078654

Contact Naisha updated successfully.

Phone Book Menu:
1. Add a New Contact
2. Update Contact Information
3. Remove a Contact
4. Check Contact Existence
5. Display All Contacts
6. Count Contacts
7. Exit

Enter your choice (1-7): 3
Enter the name of the contact to remove: Max

Contact Max removed successfully.

Phone Book Menu:
1. Add a New Contact
2. Update Contact Information
3. Remove a Contact
4. Check Contact Existence
5. Display All Contacts
6. Count Contacts
7. Exit

Enter your choice (1-7): 4
Enter the name to check: Naisha

Contact Naisha exists with phone number 89078654.

Phone Book Menu:
1. Add a New Contact
2. Update Contact Information
3. Remove a Contact
4. Check Contact Existence
5. Display All Contacts
6. Count Contacts
7. Exit

Enter your choice (1-7): 5
All contacts:
Naisha: 89078654
Tom: 8978675645
Ivy: 6789564534

Phone Book Menu:
1. Add a New Contact
2. Update Contact Information
3. Remove a Contact
4. Check Contact Existence
5. Display All Contacts
6. Count Contacts
7. Exit

Enter your choice (1-7): 6
Total number of contacts: 3

Phone Book Menu:
1. Add a New Contact
2. Update Contact Information
3. Remove a Contact
4. Check Contact Existence
5. Display All Contacts
6. Count Contacts
7. Exit

Enter your choice (1-7): 7
Exiting the program.

Phone Book Menu:
1. Add a New Contact
2. Update Contact Information
3. Remove a Contact
4. Check Contact Existence
5. Display All Contacts
6. Count Contacts
7. Exit

Enter your choice (1-7): 8
Invalid choice. Please try again.

"""