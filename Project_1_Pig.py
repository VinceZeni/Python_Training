# Project here: https://www.youtube.com/watch?v=21FnnGKSRZo&t=459s

import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

value = roll()
print(value)

while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit()
        players = int(players)