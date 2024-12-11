# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 11/12/2024
# Purpose: This script generates a username based on 
#          the user's full name. It takes the first 
#          letter of the first name, the last name, 
#          and a random number to create a unique username.
# ---------------------------------------------------

# Importing os module 
import os  
# Importing random module for generating random numbers
import random  

# Function to print the user to enter their full name
def enterName():
    # User input for full name
    fullName = input("Please Enter Your Fullname: ") 
    # Return the full name
    return fullName  

# Function to split the full name into first and last names
def splitName(fullName): 
    # Split the full name into a list of words
    name = fullName.split()  
    # The first element is the first name
    firstName = name[0]  
     # The last element is the last name
    lastName = name[-1] 
    # Return first and last name
    return firstName, lastName  

# Function to extract the first character of the first name
def firstChar(firstName):
    # Get the first character of the first name
    fChar = firstName[0]  
     # Return the first character
    return fChar 

# Function to generate a random number between 100 and 999
def randomNumber():
     # Generate a random number between 100 and 999
    number = random.randrange(100, 999) 
    # Return the random number
    return number  

# Main logic to create a username
# Prompt the user to enter their full name
fullName = enterName() 
# Split the full name into first and last names
firstName, lastName = splitName(fullName)  
# Create username
userName = firstChar(firstName).lower() + lastName + str(randomNumber())  
 # Display the generated username
#print(f"The username for {fullName} is {userName}") 
print("The username for " + fullName + " is " + userName)


