from turtle import Turtle, Screen
from random import choice

LENGHT = 100
number_of_edge = 3
color_list = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "brown",
    "gray",
    "gold",
    "cyan",
    "Gainsboro",
    "gray",
    "dimgray",
    "LightSlateGray",
    "AliceBlue",
    "LimeGreen",
    "DarkKhaki",
    "Khaki",
]

timmy_turtle = Turtle()
timmy_turtle.pensize(15)
timmy_turtle.speed(3)
# Setup turtle position
timmy_turtle.penup()
timmy_turtle.setpos(0, 100)
timmy_turtle.pendown()
should_be_continue = True
while should_be_continue:
    color_choice = choice(color_list)
    timmy_turtle.color(color_choice)
    for _ in range(number_of_edge):
        timmy_turtle.forward(LENGHT)
        timmy_turtle.right(360 / number_of_edge)
    number_of_edge += 1

    if number_of_edge > 14:
        should_be_continue = False


my_screen = Screen()
my_screen.exitonclick()
