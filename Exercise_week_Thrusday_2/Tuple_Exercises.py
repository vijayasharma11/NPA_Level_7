# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 18/12/2024
# Purpose:Create a tuple named months containing the names of all the months.
#Print the third month from the months tuple.
#Create two tuples, tuple1 and tuple2, then concatenate the two tuples and store the result in a new tuple.
#Unpack the following tuple into four variables: tuple_to_unpack = (1, 2, 3, 4).
#Write a function that takes a tuple of numbers as input and returns the sum of all elements in the tuple.
# ---------------------------------------------------

#Create a tuple named months containing the names of all the months.
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print(f"The names of all the months : \n{months}" )
print()

#Print the third month from the months tuple.
print("The third month from the months : ", months[2])
print()

#Create two tuples, tuple1 and tuple2, then concatenate the two tuples and store the result in a new tuple.
tuple1 = (1,2,3)
tuple2 = (4,5,6)
Concatenated_tuple_result = tuple1 + tuple2
print("Concatenated tuple:", Concatenated_tuple_result)
print()

#Unpack the following tuple into four variables: tuple_to_unpack = (1, 2, 3, 4).
tuple_to_unpack = (1, 2, 3, 4)
a,b,c,d = tuple_to_unpack
print("Unpacked value a : ",a)
print("Unpacked value b : ",b)
print("Unpacked value c : ",c)
print("Unpacked value d : ",d)


#Write a function that takes a tuple of numbers as input and returns 
# the sum of all elements in the tuple.
def sum_of_tuple(numbers):
    return sum(numbers)

# the sum_of_tuple function
numbers_tuple = (1, 2, 3, 4)
print("Sum of the tuple:", sum_of_tuple(numbers_tuple))

#-------------------------------------------------------------------------------------
#Output :
#The names of all the months : 
#('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')    

#The third month from the months :  March

#Concatenated tuple: (1, 2, 3, 4, 5, 6)

#Unpacked value a :  1
#Unpacked value b :  2
#Unpacked value c :  3
#Unpacked value d :  4

#Sum of the tuple: 10

#---------------------------------------------------------------------------------------------



