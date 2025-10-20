# Guess number game

import random

secret_number = random.randint(1, 20)

attempts = 0
print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 20.")
while True:
    guess = input("Take a guess: ")
    attempts += 1
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        break