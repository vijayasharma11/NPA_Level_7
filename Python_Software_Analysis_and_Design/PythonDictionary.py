# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 12/02/2025
# Purpose:a python program that will ask a user to enter a name and a score it will add this information to a dictionary, 
# you will then repeat this two more times so your dictionary should contain a total of three names and three scores, 
# it will then print this list. 
#-----------------------------------------------------------------

# Create an empty dictionary to store names and scores
scores = {}

# Ask the user for a name and score three times
name1 = input("Enter a name: ")
score1 = input("Enter a score: ")
scores[name1] = score1

name2 = input("Enter a name: ")
score2 = input("Enter a score: ")
scores[name2] = score2

name3 = input("Enter a name: ")
score3 = input("Enter a score: ")
scores[name3] = score3

# Display the dictionary
print("Names and Scores:", scores)


'''

Design/PythonDictionary.py
Enter a name: Vijaya
Enter a score: 78
Enter a name: Saumya
Enter a score: 67
Enter a name: Naisha
Enter a score: 98
Names and Scores: {'Vijaya': '78', 'Saumya': '67', 'Naisha': '98'}
PS D:\Vijaya\NPA_Level_7> 
'''