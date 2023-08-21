from turtle import Turtle,Screen
from random import randint,choice
from colors import colors

dir = [0,90,180,270]
speeds = [2,4,6,8,10]

drawer = Turtle()
drawer.shape('circle')
size_of_gap = 5
i =0
drawer.speed(200)

while(i < randint(10,20)):
    i=i + 1
    for _ in range(int(360 / size_of_gap)):
        drawer.pencolor(choice(colors))
        drawer.circle(100)
        drawer.setheading(drawer.heading() + size_of_gap)


screen = Screen()
screen.exitonclick()

