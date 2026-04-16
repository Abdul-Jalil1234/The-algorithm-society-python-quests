#!/usr/bin/python3
secret_number = 7
guess = None              # None = "no value yet" — guarantees the loop starts
 
while guess != secret_number:     # != means "not equal to"
    guess = int(input("Guess the secret number: "))
    if guess != secret_number:
        print("Not quite! Try again.")
 
print(f"Correct! The secret number was {secret_number}. Well done!")

