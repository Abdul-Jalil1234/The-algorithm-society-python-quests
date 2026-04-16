#!/usr/bin/python3

age  = int(input("How old are you? "))
gold = int(input("How many gold coins do you have? "))
 
if age >= 18 and gold >= 20:
    print("You may enter the club. Enjoy!")
elif age < 18 and gold >= 20:
    print("Sorry, you need to be 18+ to enter.")
elif age >= 18 and gold < 20:
    print("Sorry, you need at least 20 gold coins.")
else:
    print("Sorry, you meet neither requirement.")

