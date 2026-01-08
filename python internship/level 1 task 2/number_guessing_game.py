import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it.")

    secret_number = random.randint(1, 100)
    print(f"DEBUG: Secret number is {secret_number}")
    attempts = 10

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempt} attempts!")
            return
        
        diff = guess - secret_number
        if diff > 10:
            print("Too high!")
        elif diff > 0:
            print("High!")
        elif diff < -10:
            print("Too low!")
        else: # -10 <= diff < 0
            print("Low!")

    print(f"Game Over! The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
                                # thank you