# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 06/02/2025
# Purpose: a python program to work as a calculator, 
# you should use functions, if statements, user inputs operators and print functions.
#-----------------------------------------------------------------
# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main function to run the calculator
def calculator():
    while True:  # This loop will repeat until the user chooses to exit
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Get user input for operation
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break  # Exit the loop and stop the program

        # Get user input for numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue  # Go back to the start of the loop

        # Perform the calculation based on user choice
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input! Please choose a valid operation.")

        # Ask the user if they want to perform another calculation
        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Exiting calculator. Goodbye!")
            break  # Exit the loop and stop the program

# Run the calculator
calculator()
