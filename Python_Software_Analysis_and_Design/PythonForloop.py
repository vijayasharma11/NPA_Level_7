# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 12/02/2025
# Purpose:program you created for the dictionary task you will develop a python program 
# that will ask a user how many grades they are going to enter, 
# then loops through the process of collecting the names and grades 
# that amount of times storing them in a dictionary it will then print this dictionary. 
#-----------------------------------------------------------------


# Create an empty dictionary to store names and scores
scores = {}

# Ask the user how many grades they want to enter
num_grades = int(input("How many grades will you enter? "))

# Loop to collect names and scores
for _ in range(num_grades):
    name = input("Enter a name: ")
    score = input("Enter a score: ")
    scores[name] = score

# Display the dictionary
print("Names and Scores:", scores)

'''
Design/PythonForloop.py
How many grades will you enter? 4
Enter a name: Vijaya
Enter a score: 89
Enter a name: Saumya
Enter a score: 67
Enter a name: Naisha  
Enter a score: 78
Enter a name: Bharat
Enter a score: 88
Names and Scores: {'Vijaya': '89', 'Saumya': '67', 'Naisha': '78', 'Bharat': '88'}
PS D:\Vijaya\NPA_Level_7> 
'''