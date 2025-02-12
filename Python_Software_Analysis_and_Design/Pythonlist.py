# Ask the user for their top 3 favorite films
favorite_films = []
for i in range(3):
    film = input(f"Enter your #{i+1} favorite film: ")
    favorite_films.append(film)

# Print the list of top 3 favorite films
print("Your top 3 favorite films are:", favorite_films)

# Ask for 2 more favorite films
more_films = []
for i in range(2):
    film = input(f"Enter your next favorite film #{i+4}: ")
    more_films.append(film)

# Combine the lists
top_5_films = favorite_films + more_films

# Print out the updated list of top 5 favorite films
print("Your top 5 favorite films are:", top_5_films)


'''
Design/Pythonlist.py
Enter your #1 favorite film: Inception
Enter your #2 favorite film: The Dark Knight  
Enter your #3 favorite film: Interstellar  
Your top 3 favorite films are: ['Inception', 'The Dark Knight  ', 'Interstellar  ']
Enter your next favorite film #4: The Matrix  
Enter your next favorite film #5: Fight Club 
Your top 5 favorite films are: ['Inception', 'The Dark Knight  ', 'Interstellar  ', 'The Matrix  ', 'Fight Club ']
PS D:\Vijaya\NPA_Level_7> 


''''

