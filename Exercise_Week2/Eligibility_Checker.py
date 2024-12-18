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
