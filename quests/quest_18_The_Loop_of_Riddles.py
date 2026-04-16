#!/usr/bin/python3
import random


secret_number = random.randint(1, 20)
guess = 0

print("I'm thinking of a number between 1 and 20.")


while guess != secret_number:
    try:
        guess = int(input("What's your guess? "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Exactly! {secret_number} was the secret number.")

    except ValueError:
        print("Oops! Please enter a whole number.")

print("Thanks for playing!")


