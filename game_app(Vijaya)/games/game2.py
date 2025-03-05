# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 12/02/2025
# Purpose:create a simple Rock-Paper-Scissors game, where the player competes against the computer. 
# The game randomly selects one of the three options (rock, paper, or scissors) for the computer, 
# while the player inputs their choice. The game then determines the winner based on standard 
# Rock-Paper-Scissors rules and assigns a score accordingly.
#-----------------------------------------------------------------

import random  # Importing the random module to allow the computer to make a random choice

def play():
    """A simple rock-paper-scissors game that returns a score."""
    
    print("\nWelcome to Rock, Paper, Scissors!")  # Greeting message

    # List of possible choices
    choices = ["rock", "paper", "scissors"]

    # Computer selects a random choice
    computer_choice = random.choice(choices)
    
    # Player input
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Validate user input
    if user_choice not in choices:
        print("Invalid choice. You lose!")  # If input is not valid, player loses
        return 0  # Return a score of 0 for an invalid choice
    
    # Display computer's choice
    print(f"Computer chose: {computer_choice}")

    # Check for a tie
    if user_choice == computer_choice:
        print("It's a tie!")
        return 50  # Tie gives 50 points

    # Check for winning conditions
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        return 100  # Win gives 100 points

    # If none of the above, the player loses
    else:
        print("You lose!")
        return 0  # Loss gives 0 points
