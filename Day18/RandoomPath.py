from turtle import Turtle,Screen
from random import randint,choice
from colors import colors

dir = [0,90,180,270]
speeds = [2,4,6,8,10]

drawer = Turtle()
drawer.shape('circle')

i =0

while(i < randint(50,200)):
    i=i + 1
    drawer.pensize(randint(10,15))
    drawer.setheading(choice(dir))
    drawer.pencolor(choice(colors))
    drawer.speed(choice(speeds))
    drawer.fd(50)

screen = Screen()
screen.exitonclick()