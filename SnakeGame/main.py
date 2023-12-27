from turtle import Turtle, Screen
import random
import time
from Food import *
from Snake import *
from Scoreboard import *

s=Screen()
s.bgcolor("black")
s.screensize(300,300)
s.tracer(0)

snake=Snake()
snake.create_snake()
s.update()

game_is_on = True




s.onkey(snake.left, "Left")
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.right, "Right")

s.update()
time.sleep(0.1)

# Code related to food
f=Food()
sc=0

score=Scoreboard()
s.listen()
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(f)<15:
        snake.extend()
        f.random_loc()
        score.increase()

    if (snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 250 or snake.head.ycor() < -250):
        game_is_on = False
        score.game_over()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            game_is_on = False
            score.game_over()

s.exitonclick()
