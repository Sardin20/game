import random
import sys

def main():
    """Main function to run the Guess the Number game."""
    print("Welcome to the Guess the Number Game!")
    print("I have picked a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    # Get guesses from command-line arguments
    if len(sys.argv) < 2:
        print("No guesses provided! Pass guesses as parameters.")
        sys.exit(1)

    guesses = sys.argv[1:]  # Read arguments passed after `python3 app.py`
    for guess in guesses:
        try:
            guess = int(guess)
            attempts += 1

            if guess < secret_number:
                print(f"Guess {guess} is too low!")
            elif guess > secret_number:
                print(f"Guess {guess} is too high!")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print(f"Invalid guess: {guess}. Please provide numbers only.")
    else:
        print(f"You did not guess the number. The correct number was {secret_number}.")

if __name__ == "__main__":
    main()
