# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 18/12/2024
# Purpose: creating a program to check whether a person is eligible to vote and drive
#  based on their age and citizenship. The eligibility criteria are as follows:#
#To vote, a person must be at least 18 years old and a citizen.
#To drive, a person must be at least 16 years old and a citizen.
#Prompt the user to enter their age and citizenship status (as "citizen" or "non-citizen").
#Check if the person is eligible to vote and drive based on the provided age and citizenship status.
#Print appropriate messages indicating whether the person is eligible to vote and drive or not.
# ---------------------------------------------------

#Function to check the Eligibility Checker
def checker_eligibility(age,citizenship):
   # Check if the user is eligible to vote
    if age >= 18 and citizenship == "citizen" :
        print("You are eligible to vote. ")
    else:
        print("You are not eligible to vote")

    # Check if the user is eligible to vote
    if age >=16 and citizenship == "citizen" :
        print("You are eligible to drive.")
    else:
        print("You are not eligible to drive.")

#main program
def main():
    age = int(input("Please enter your age :"))
    citizenship = input("Enter your citizenship status(citizen/non-citizen) : ").lower 

    checker_eligibility(age,citizenship)  

#Run main program
if __name__ == "__main__" :
    main()         


#Output :
#-------------------------------------------------------------------
#Please enter your age :12
#Enter your citizenship status(citizen/non-citizen) : citizen
#You are not eligible to vote
#You are not eligible to drive.

#Please enter your age :45
#Enter your citizenship status(citizen/non-citizen) : citizen
#You are not eligible to vote
#You are not eligible to drive.

#--------------------------------------------------------------------------
