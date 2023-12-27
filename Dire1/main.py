import colorgram
from turtle import Turtle, Screen
import random
color = colorgram.extract('image.jpg',30)


rgb_color=[]
for i in color:
    r=i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    print((r,g,b))
    rgb_color.append((r,g,b))
print(rgb_color)

my_screen=Screen()
timmy=Turtle()
my_screen.colormode(255)

timmy.speed("fastest")
# sel=random.choice(rgb_color)
# print(f"Selected {sel[0]}")
# timmy.pencolor((sel))
#timmy.pencolor((int(sel[0]),int(sel[1]),int(sel[2])))
timmy.pencolor("white")
timmy.right(90)
timmy.forward(230)
timmy.right(90)
timmy.forward(200)
timmy.left(180)
for i in range(10):
    for j in range(10):
        ch=random.choice(rgb_color)
        print(f"Selected {ch}")
        timmy.pencolor(ch)
        timmy.fillcolor(ch)
        timmy.begin_fill()
        timmy.circle(10)
        timmy.end_fill()
        timmy.pencolor("white")
        timmy.forward(50)
    timmy.pencolor("white")
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.left(180)


my_screen.exitonclick()
