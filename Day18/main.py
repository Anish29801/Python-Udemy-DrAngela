from turtle import Turtle,Screen

drawer = Turtle()

drawer.shape('arrow')

i = 0
while (i < 4):
    drawer.forward(100)
    drawer.right(90)
    i += 1 

screen = Screen()
screen.exitonclick()