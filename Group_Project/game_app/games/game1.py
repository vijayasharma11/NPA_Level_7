import random
def play():
    """A simple number guessing game that returns a score."""
    print("\nWelcome to Guess the Number!")
    number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1
            if guess == number:
                print(f"Correct! You guessed in {attempts} attempts.")
                return 100 - (attempts * 10)
            elif guess < number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")