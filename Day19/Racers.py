from turtle import Turtle, Screen
from random import randint


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
racers = []

#Create 6 racers
for turtle_index in range(0, 6):
    new_racer = Turtle(shape="arrow")
    new_racer.penup()
    new_racer.color(colors[turtle_index])
    new_racer.goto(x=-230, y=y_positions[turtle_index])
    racers.append(new_racer)

if (user_bet and user_bet != ''):
    is_race_on = True
else:
    s_race_on = False

while is_race_on:
    for turtle in racers:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        turtle.forward(randint(0, 10))

screen.exitonclick()