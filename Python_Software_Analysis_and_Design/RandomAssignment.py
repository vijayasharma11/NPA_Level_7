# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 14/02/2025
# Purpose: Python program selects a random movie from a list of films using the random module and prints the chosen movie.
#-----------------------------------------------------------------

import random

# List of films
films = [
    "Inception",
    "The Matrix",
    "Interstellar",
    "The Dark Knight",
    "Titanic",
    "The Dark Knight",
    "Avatar",
    "The Godfather",
    "The Batman"
]

# Select a random film
random_film = random.choice(films)

# Print the randomly selected film
print("The randomly selected film is:", random_film)


'''
Design/RandomAssignment.py
The randomly selected film is: The Godfather
'''