from turtle import Turtle, Screen
from turtle import *
import random

color_list=['blue','red','green','purple','indigo','orange']
s=Screen()
s.screensize(canvwidth=300,canvheight=300)

user_bet=numinput("Who will win?", "Choose 1 - blue, 2 - red', 3 - green, 4 - purple, 5 - indigo , 6 - orange 1-6",3,1,6)
user_bet=int(user_bet)-1
print(f"Bet on {color_list[user_bet]}")

def random_speed():
    return random.choice(range(9))

def random_steps():
    return random.choice(range(10,60))

def start_the_race(t_list):

    for i in range(6):
        r=random_steps()
        x,y = t_list[i].position()
        if r> 300-x:
            r=300-x
        else:
            r
        t_list[i].forward(r)
        print(f"After steps position is {t_list[i].position()}")

    return t_list

def who_won(n):
    print(f"Player {n+1} won")
    if user_bet+1==n+1:
        print("You won the bet")
    else:
        print("You lost the bet")
    return True


def player_position(t_list):
    pos=[]
    for i in range(6):
        pos.append(t_list[i].position())
    print(f"Position is {pos}")
    win=0
    for (x,y) in pos:
        if x==300:
            found_winner = who_won(win)
            break
        else:
            win += 1

        found_winner=False
    if found_winner:
        return False
    else:
        return True


t_list=[]
y=150
sp_list=[]
for i in range(6):
    t=Turtle(shape='turtle')
    t_list.append(t)
    t.penup()
    t.color(color_list[i])
    t.goto(x=-290,y=y)
    y-=45
    sp=random_speed()
    sp_list.append(sp)


cont=True
while cont:
    t_list=start_the_race(t_list)
    cont=player_position(t_list)


s.exitonclick()
