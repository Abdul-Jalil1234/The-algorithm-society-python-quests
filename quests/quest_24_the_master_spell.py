#!/usr/bin/python3
def ask_for_age():
    age = int(input("Please enter your age: "))
    return age                  # hand the number back to the caller
 
def can_they_vote(age):
    if age >= 18:
        print(f"At {age} years old, you are eligible to vote!")
    else:
        print(f"At {age} years old, you cannot vote yet. Come back in {18 - age} year(s).")
 
user_age = ask_for_age()        # step 1: get the age
can_they_vote(user_age)         # step 2: use it

