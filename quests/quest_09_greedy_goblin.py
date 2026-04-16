#!/usr/bin/python3
gold_pieces = 27
friends     = 4
 
each_gets    = gold_pieces // friends   # 6  — no decimals, can't split a coin
goblin_keeps = gold_pieces % friends    # 3  — remainder after fair sharing
 
print(f"Each friend gets {each_gets} gold pieces.")
print(f"The goblin keeps {goblin_keeps} gold pieces. Sneaky goblin!")

