# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 05/02/2025
# Purpose: Implement a Python function that takes user input for two numbers and an 
# operation and performs the corresponding mathematical operation 
# while handling various exceptions gracefully.
#-----------------------------------------------------------------

def perform_operation():
    while True:
        try:
            # Input: First number
            num1 = float(input("Enter the first number: "))
            
            # Input: Second number
            num2 = float(input("Enter the second number: "))
            
            # Input: Operation
            operation = input("Enter the operation (+, -, *, /): ")
            
            # Validate operation and perform calculation
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                # Check for division by zero
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2
            else:
                # Handle invalid operation input
                raise ValueError("Invalid operation. Please choose +, -, *, or /.")
            
            # Display the result and break the loop
            print(f"Result: {result}")
            break
            
        except ValueError as ve:
            print(f"Error: {ve}. Please try again.")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

# Example call to the function
perform_operation()


'''
OUTPUT:
Enter the first number: 3
Enter the second number: 4
Enter the operation (+, -, *, /): +
Result: 7.0
Enter the first number: 56
Enter the second number: 0
Enter the operation (+, -, *, /): /
Error: Cannot divide by zero.. Please try again.
Enter the first number: 54
Enter the second number: 65
Enter the operation (+, -, *, /): *
Result: 3510.0
'''