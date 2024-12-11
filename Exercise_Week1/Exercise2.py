# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 11/12/2024
# Purpose: Count Vowels Write a Python function
# that takes a string as input and returns 
# the count of vowels in that string. 
# For example, if the input is "hello", 
# the function should return 2..
# ---------------------------------------------------

#function define Count_vowels
def count_vowels(input_string):
    #define lower and upper case vowels
    vowels = "aeiouAEIOU"
    #initialize the counter
    count = 0
    for char in input_string :
        #check if the character is vowel
        if char in vowels :
            #increment the count if it's vowel
            count+= 1
    return count

input_string = "hello"
result =count_vowels(input_string)
print(f"The number of vowels in '{input_string}' is {result}")        
