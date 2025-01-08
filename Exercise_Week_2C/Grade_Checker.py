# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 13/12/2024
# Purpose: 
# Create a list named student_scores containing the following scores: 70, 45, 85, 30, 65.
#Iterate through each score in the student_scores list.
#For each score, use the ternary operator to print "Pass" 
# if the score is greater than or equal to 60, and "Fail" otherwise.
# ---------------------------------------------------

# List of student scores
student_scores = [70, 45, 85, 30, 65]

# Iterate through each score and use a ternary operator to check if it's a pass or fail
for score in student_scores:
    # Ternary operator to check if the score is a passing grade or not
    print(f"Score: {score} - {'Pass' if score >= 60 else 'Fail'}")


#Output
#-----------------------------------------------------
#Score: 70 - Pass
#Score: 45 - Fail
#Score: 85 - Pass
#Score: 30 - Fail
#Score: 65 - Pass

#-----------------------------------------------------------