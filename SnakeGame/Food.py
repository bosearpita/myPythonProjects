import random
from turtle import Turtle

class Food(Turtle):



    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.random_loc()

    def random_loc(self):
        f_x = random.randint(-130, 130)
        f_y = random.randint(-130, 130)
        self.goto(f_x, f_y)


