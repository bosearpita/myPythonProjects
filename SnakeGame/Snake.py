from turtle import Turtle, Screen
import random
import time

s=Screen()
s.tracer(0)


STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=10
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake():
    def __init__(self):
        self.segments=[]
        self.create_snake()

        self.head=self.segments[0]
        self.tail=self.segments[-1]
        
    
    
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.increase_size(pos)
            
        
    def right(self):
        
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def left(self):

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.left(180)
        self.head.forward(MOVE_DISTANCE)

    def move(self):

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def increase_size(self,pos):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(pos)
        self.segments.append(t)

    def extend(self):
        self.increase_size(self.segments[-1].position())