# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 18/12/2024
# Purpose: Write a Python program to do the following using array module:
#Create an array named my_array containing integers from 1 to 10.
#Print the contents of my_array.
#Find and print the length of my_array.
#Print the sum of all elements in my_array.
#-----------------------------------------------------------------

import array

#Create an array named my_array containing integers from 1 to 10.
my_array  = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


#Print the contents of my_array.
print("Contents of my_array. : ", my_array)
print()

#Find and print the length of my_array.
print("The length of my_array is : ", len(my_array))
print()

#Print the sum of all elements in my_array.
print("The sum of all elements in my_array is :",sum(my_array))


#Output
#------------------------------------------------------------------------------
#Contents of my_array. :  array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#The length of my_array is : 10

#The sum of all elements in my_array is : 55

#--------------------------------------------------------