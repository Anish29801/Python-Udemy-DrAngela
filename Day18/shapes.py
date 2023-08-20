from turtle import Turtle,Screen

drawer = Turtle()

colors = ['red', 'green', 'blue', 'violet', 'orange', 'yellow', 'aqua','purple']

drawer.shape('classic')


def PolyDrawer(sides):
    i = 0
    drawer.pencolor(colors[sides -3])
    while(i < sides):
       drawer.fd(100)
       drawer.right(360/sides) 
       i = i + 1

sides = 3
while(sides >= 3 and sides <=10):       
    PolyDrawer(sides)
    sides = sides + 1


screen = Screen()
screen.exitonclick()