import csv
import games.game1 as game1
import games.game2 as game2
from utils import display_high_scores, export_scores

SCORES_FILE = "scores.csv"

def save_score(name, score):
    """Saves the player's score to the CSV file."""
    with open(SCORES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, score])

def main_menu():
    while True:
        print("\nWelcome to Glasgow Code Learning Game App!")
        print("1. Play Game 1")
        print("2. Play Game 2")
        print("3. View High Scores")
        print("4. Export Scores to CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter your name: ")
            score = game1.play()  # Assuming game1.play() returns a score
            save_score(name, score)
        elif choice == "2":
            name = input("Enter your name: ")
            score = game2.play()
            save_score(name, score)
        elif choice == "3":
            display_high_scores(SCORES_FILE)
        elif choice == "4":
            export_scores(SCORES_FILE)
        elif choice == "5":
            print("Exiting... Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
