from turtle import Turtle, Screen
from random import randint
import turtle

sqirograph_turtle = Turtle()
sqirograph_turtle.pensize(5)
turtle.colormode(255)
# Draw a circle with a specified radius
RADIUS = 200
# sqirograph_turtle.circle(RADIUS)
sqirograph_turtle.speed(0)  # 0 = fastest


def rgb_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rbg_value = (r, g, b)
    return rbg_value


# Draw a spirograph
for i in range(0, 360, 10):
    sqirograph_turtle.pencolor(rgb_color())
    sqirograph_turtle.right(10)
    sqirograph_turtle.circle(RADIUS)

my_screen = Screen()
my_screen.colormode(255)
my_screen.exitonclick()
