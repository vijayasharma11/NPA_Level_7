# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 12/02/2025
# Purpose:This program is a game application menu system that allows users to play different games, 
# save their scores, and view or export their score history. It serves as a central hub for 
# managing multiple games and tracking player performance.
#-----------------------------------------------------------------
import csv  # Import CSV module to handle score storage
import games.game1 as game1  # Import Game 1 module
import games.game2 as game2  # Import Game 2 module
from utils import display_high_scores, export_scores  # Import utility functions

# File name where scores are stored
SCORES_FILE = "scores.csv"

def save_score(name, score):
    """Saves the player's score to the CSV file."""
    with open(SCORES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, score])  # Append player's name and score to the file

def main_menu():
    """Displays the main menu and handles user input to play games or manage scores."""
    while True:
        # Display main menu options
        print("\nWelcome to Glasgow Code Learning Game App!")
        print("1. Play Game 1")
        print("2. Play Game 2")
        print("3. View High Scores")
        print("4. Export Scores to CSV")
        print("5. Exit")

        # Get user's menu choice
        choice = input("Enter your choice: ")
        
        # Play Game 1
        if choice == "1":
            name = input("Enter your name: ")
            score = game1.play()  # Assuming game1.play() returns a score
            save_score(name, score)  # Save the player's score

        # Play Game 2
        elif choice == "2":
            name = input("Enter your name: ")
            score = game2.play()
            save_score(name, score)  # Save the player's score

        # View high scores
        elif choice == "3":
            display_high_scores(SCORES_FILE)  # Call function to display high scores

        # Export scores to a CSV file
        elif choice == "4":
            export_scores(SCORES_FILE)  # Call function to export scores

        # Exit the application
        elif choice == "5":
            print("Exiting... Thank you for playing!")
            break  # Exit the loop and end the program

        # Handle invalid input
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main menu when the script is executed
if __name__ == "__main__":
    main_menu()
