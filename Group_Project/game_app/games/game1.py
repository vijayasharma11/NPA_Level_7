# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 12/02/2025
# Purpose:Create a simple number guessing game where the player tries to guess a randomly chosen number between 1 and 10. 
# The program provides feedback on whether the guess is too high or too low and keeps track of the number of attempts. 
# The final score is calculated as 100 minus (10 times the number of attempts), 
# rewarding fewer attempts with a higher score.
#-----------------------------------------------------------------

import random  # Importing the random module to generate a random number

def play():
    """A simple number guessing game that returns a score."""
    
    print("\nWelcome to Guess the Number!")  # Display a welcome message

    # Generate a random number between 1 and 10
    number = random.randint(1, 10)
    attempts = 0  # Initialize the attempt counter

    while True:  # Infinite loop until the correct number is guessed
        try:
            # Get user input and convert it to an integer
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1  # Increase attempt counter

            # Check if the guess is correct
            if guess == number:
                print(f"Correct! You guessed in {attempts} attempts.")
                return 100 - (attempts * 10)  # Score decreases with more attempts

            # Give a hint if the guess is too low
            elif guess < number:
                print("Too low! Try again.")

            # Give a hint if the guess is too high
            else:
                print("Too high! Try again.")

        # Handle cases where the user enters a non-numeric value
        except ValueError:
            print("Invalid input. Please enter a number.")  
