import random

def play():
    """A simple rock-paper-scissors game that returns a score."""
    print("\nWelcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. You lose!")
        return 0
    
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
        return 50
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        return 100
    else:
        print("You lose!")
        return 0