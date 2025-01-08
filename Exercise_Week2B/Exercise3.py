# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 11/12/2024
# Purpose: Leap Year Checker Write a Python function
#  that takes a year as input and returns True 
# if it is a leap year, and False otherwise. 
# A leap year is divisible by 4, 
# but not by 100 unless it is also divisible by 400.
# ---------------------------------------------------
#function to implement conditions to check leap year  
def check_leap(year):
    # If the year is divisible by 4 and not divisible by 100, or divisible by 400, it's a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
         print("Given Year is a leap Year");  
        # Else it is not a leap year  
    else:  
        print ("Given Year is not a leap Year")  
# Taking an input year from user  
Year = int(input("Enter the number: "))  
# Printing result  
check_leap(Year) 