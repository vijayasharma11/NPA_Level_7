
# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 11/12/2024
# Purpose: Reverse String Write a Python function
# that takes a string as input and returns
#  the reverse of that string. For example,
#  if the input is "hello", the function should return "olleh".e.
# ---------------------------------------------------

#Function to writ reverse String
def reverse_string(input_string):
     # Return the reversed string using slicing
    return input_string[::-1]


result =reverse_string("hello")
print(result)
