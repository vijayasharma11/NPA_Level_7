# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 04/02/24
# Purpose:a python program to calculate grades, 
# it should take a number between 0 and 100 from the user and provide 
# a letter grade based upon that number using If / else ifs and else statements
# -----------------------------------------

# Ask the user to enter a number between 0 and 100
score = float(input("Please enter your score (0 to 100): "))

#Check the score and assign the corresponding letter grade using if-else statements
if 90 <= score <= 100:
    grade = "A"
elif 70 <= score <= 89:
    grade = "B"
elif 50 <= score <= 69:
    grade = "C"
elif 40 <= score <= 49:
    grade = "D"
elif 0 <= score <= 39:
    grade = "Fail"
else:
    grade = "Invalid score. Please enter a number between 0 and 100."

#Display the result
print(f"Your score is {score}, and your grade is: {grade}")
