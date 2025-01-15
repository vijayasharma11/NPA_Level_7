# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 15/01/2025
# Purpose: List Statistics (Lambda Functions).
#-----------------------------------------------------------------

#Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#lambda function to  squares a number.
square = lambda x : x ** 2

# Create a list of squared numbers using the map function
squared_numbers = list(map(square, numbers))

#Find the minimum and maximum values of the squared numbers

min_squared = min(squared_numbers)
max_squared = max(squared_numbers)

# Print the results
print(f"Original list: {numbers}")
print(f"Squared numbers: {squared_numbers}")
print(f"Minimum squared number: {min_squared}")
print(f"Maximum squared number: {max_squared}")


"""
Output:
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Squared numbers: [1, 4, 9, 16, 25, 36, 49, 64, 81]
Minimum squared number: 1
Maximum squared number: 81
"""