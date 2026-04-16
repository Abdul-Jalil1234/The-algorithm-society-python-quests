#!/usr/bin/python3
def start():
    print("\n=== The Forgotten Forest ===")
    print("You stand at the edge of a dark forest.")
    choice = input("Do you enter the forest or take the mountain path? ").lower()
 
    if "forest" in choice or "enter" in choice:
        dark_forest()
    else:
        mountain_path()
 
def dark_forest():
    print("\n=== Deep in the Dark Forest ===")
    print("You find a glowing door and an old well.")
    choice = input("Do you open the door or look into the well? ").lower()
 
    if "door" in choice:
        ending_treasure()
    else:
        ending_trapped()
 
def mountain_path():
    print("\n=== The Mountain Path ===")
    print("You meet a wise old wizard who offers you a choice.")
    choice = input("Accept his magic staff or continue alone? ").lower()
 
    if "staff" in choice or "accept" in choice:
        ending_hero()
    else:
        ending_lost()
 
def ending_treasure():
    print("\nENDING: The door leads to an ancient vault full of treasure!")
    print("You retire as the wealthiest adventurer in the land. THE END.")
 
def ending_trapped():
    print("\nENDING: The well is a portal to another dimension!")
    print("You are trapped forever, but at least it's interesting. THE END.")
 
def ending_hero():
    print("\nENDING: The magic staff grants you power to defeat the Dark Lord!")
    print("The kingdom cheers your name. THE END.")
 
def ending_lost():
    print("\nENDING: You wander the mountain alone, and become a legend of mystery.")
    print("No one knows what happened to you. THE END.")
 
start()

