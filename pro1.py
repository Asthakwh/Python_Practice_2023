import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("enter the number of players(1-4)")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("must be 2 -4 ")
    else:
        print("invalid")

max_score = 50
players_score =[0 for _ in range(players)]
print(players_score)
