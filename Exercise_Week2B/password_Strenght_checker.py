# Header Section
# ----------------------------------------------------------------------------------
# Name: Vijaya Sharma
# Date: 11/12/2024
# Purpose: Python program that checks the strength of a password entered by the user. 
# The program should evaluate the password based on various criteria such as length, 
# presence of both uppercase and lowercase letters, numbers, and special characters. 
# It should provide feedback to the user about the strength of their password..
# ------------------------------------------------------------------------------------

import string

#Constants for the minimum length
MIN_UPPERCASE = 1
MIN_LOWERCASE = 1
MIN_DIGIT = 1
MIN_SPECIAL_CHAR = 1
MIN_LENGTH = 8

#Function to chacke password strength
def count_characters(password):
    count_uppercase = 0
    count_lowercase = 0
    count_digits = 0
    count_special_char = 0

    #iterate through each character in the password and check its type.
    for char in password :
        if char.isupper():
            count_uppercase += 1
        elif char.islower():
            count_lowercase += 1
        elif char.isdigit():
            count_digits += 1    
        elif char in string.punctuation :
            count_special_char += 1
    return count_uppercase, count_lowercase, count_digits, count_special_char

# Function to check if the password length is sufficient
def check_length(password):
    return len(password) >= MIN_LENGTH

 # Function to check the other password requirements
def check_requirements(count_uppercase, count_lowercase, count_digits, count_special_char):
    is_strong = True
    messages = []

    if count_uppercase < MIN_UPPERCASE :     
        print(f"Password needs at least {MIN_UPPERCASE} uppercase letter(s).")
        is_strong = False
    if count_lowercase < MIN_LOWERCASE :
        print(f"Password needs at least {MIN_LOWERCASE} lowercase letter(s).")
        is_strong = False
    if count_digits < MIN_DIGIT:
        print(f"Password needs at least {MIN_DIGIT} digit (s).")
        is_strong = False
    if count_special_char <  MIN_SPECIAL_CHAR:
        print(f"Password needs at least {MIN_SPECIAL_CHAR} Special Character (s).")
        is_strong = False
    return is_strong, messages

# Function to check the password strength
def check_password_strength(password):
    is_strong = True
    messages = []

    #check the password length
    if not check_length(password):
        messages.append(f"Password is too short! Minimum length required is {MIN_LENGTH}.")
        is_strong = False

    # Count characters in the password
    count_uppercase, count_lowercase, count_digits, count_special_char = count_characters(password)

    # Check other requirements
    is_strong, requirement_messages = check_requirements(count_uppercase, count_lowercase, count_digits, count_special_char)
    messages.extend(requirement_messages)
    
    # Provide feedback based on the evaluation
    if is_strong:
        print("\nPassword Strength: Strong")
        print("Congratulations! Your password meets the minimum requirements.")
    else:
        print("\nPassword Strength: Weak")
        print("Please improve your password to meet all the required criteria.")
        for message in messages:
            print(message)
#Main function
def main():
    print("Welcome to the Password Strength Checker!")
    password = input("Please enter your password: ")
    print("\nChecking password strength...\n")
    check_password_strength(password)

# Run the program
if __name__ == "__main__":
    main()