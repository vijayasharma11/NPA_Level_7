# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 12/02/2025
# Purpose:python program that will ask a user if they want to enter grades, 
# if the user types Yes it will ask for the name and grade, 
# it will ask if they want to add another grade and it will keep allowing them 
# to add grades until they reply No.
#-----------------------------------------------------------------

# Create an empty dictionary to store names and scores
scores = {}

# Ask the user if they want to enter grades
while True:
    add_grade = input("Do you want to enter a grade? (Yes/No): ").strip().lower()
    if add_grade == "no":
        break
    elif add_grade == "yes":
        name = input("Enter a name: ")
        score = input("Enter a score: ")
        scores[name] = score
    else:
        print("Please enter Yes or No.")

# Display the dictionary
print("Names and Scores:", scores)

'''
Do you want to enter a grade? (Yes/No): 4
Please enter Yes or No.
Do you want to enter a grade? (Yes/No): yes
Enter a name: Vijaya
Enter a score: 67
Do you want to enter a grade? (Yes/No): yes
Enter a name: saumya
Enter a score: 77
Do you want to enter a grade? (Yes/No): no
Names and Scores: {'Vijaya': '67', 'saumya': '77'}
PS D:\Vijaya\NPA_Level_7> 
'''