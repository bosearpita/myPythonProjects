from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.write(f"Score : = {self.score}", False, align="center")

    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"Score : = {self.score}", False, align="center")

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!", False, align="center")
