# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 04/02/24
# Purpose:You will develop a python program that will ask the user to enter a name, 
# ask them to enter two numbers and add them together and then display the answer to them.
#-------------------------------------------------------------
# Ask for the user's name
name = input("Please enter your name: ")

# Ask for two numbers
first_number = float(input("Enter the first number: "))  
second_number = float(input("Enter the second number: ")) 

# Add the two numbers together
sum_result = first_number + second_number

# Display the result
print(f"Hello {name}, when added together your numbers are equal to {sum_result}")
