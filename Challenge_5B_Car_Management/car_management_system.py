# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 012/02/2025
# Purpose: The purpose of this Car Management System is to allow users to efficiently manage car
#  details using a menu-driven interface Add Car Details – Store details such as registration number, make, model, and year in a dictionary.
#Delete Car Details – Remove car information using the registration number.
#Find Car Details – Retrieve and display details of a specific car.
#Ensure Data Integrity – Utilize error handling to prevent invalid inputs, ensuring robustness and usability.
#--------------------------------------------- --------------------

def add_car_details(cars):
    try:
        reg_number = input("Enter registration number: ").strip()
        if reg_number in cars:
            print("Car with this registration number already exists.")
            return
        make = input("Enter car make: ").strip()
        model = input("Enter car model: ").strip()
        year = int(input("Enter car year: "))
        cars[reg_number] = {'make': make, 'model': model, 'year': year}
        print("Car details added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

def delete_car_details(cars):
    reg_number = input("Enter registration number to delete: ").strip()
    if reg_number in cars:
        del cars[reg_number]
        print("Car details deleted successfully.")
    else:
        print("Car not found.")

def find_car_details(cars):
    reg_number = input("Enter registration number to find: ").strip()
    if reg_number in cars:
        car = cars[reg_number]
        print(f"Car Details - Make: {car['make']}, Model: {car['model']}, Year: {car['year']}")
    else:
        print("Car not found.")

def menu():
    cars = {}
    while True:
        print("\nCar Management System")
        print("1. Add Car Details")
        print("2. Delete Car Details")
        print("3. Find Car Details")
        print("4. Exit Application")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_car_details(cars)
        elif choice == '2':
            delete_car_details(cars)
        elif choice == '3':
            find_car_details(cars)
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    menu()


'''Output:

Car Management System
1. Add Car Details
2. Delete Car Details
3. Find Car Details
4. Exit Application
Enter your choice: 1
Enter registration number: ABC123
Enter car make: Toyota
Enter car model: Corolla
Enter car year: 2020
Car details added successfully.

Car Management System
1. Add Car Details
2. Delete Car Details
3. Find Car Details
4. Exit Application
Enter your choice: 3
Enter registration number to find: ABC123
Car Details - Make: Toyota, Model: Corolla, Year: 2020

Car Management System
1. Add Car Details
2. Delete Car Details
3. Find Car Details
4. Exit Application
Enter your choice: 2
Enter registration number to delete: ABC123
Car details deleted successfully.

Car Management System
1. Add Car Details
2. Delete Car Details
3. Find Car Details
4. Exit Application
Enter your choice: 4
Exiting application. Goodbye!


'''