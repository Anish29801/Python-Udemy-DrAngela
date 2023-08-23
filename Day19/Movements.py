from turtle import Turtle, Screen

drawer = Turtle()
screen = Screen()


def mvright():
    drawer.forward(10)

def mvleft():
    drawer.backward(10)

def turn_left():
    new_heading = drawer.heading() + 10
    drawer.setheading(new_heading)

def turn_right():
    new_heading = drawer.heading() - 10
    drawer.setheading(new_heading)

def clear():
    drawer.clear()
    drawer.penup()
    drawer.home()
    drawer.pendown()

screen.listen()
screen.onkey(mvright, "Up")
screen.onkey(mvleft, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "space")

screen.exitonclick()
