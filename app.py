import random

def main():
    """Main function to run the Guess the Number game."""
    print("Welcome to the Guess the Number Game!")
    print("I have picked a number between 1 and 100.")
    print("Try to guess it!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get the user's guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
