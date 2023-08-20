from turtle import Turtle,Screen

drawer = Turtle()

drawer.shape('arrow')
drawer.backward(60)

i = 0
while (i < 8):  
    i=i + 1
    drawer.pencolor('black')
    drawer.forward(20)
    drawer.pencolor('white')
    drawer.forward(20)


screen = Screen()
screen.exitonclick()