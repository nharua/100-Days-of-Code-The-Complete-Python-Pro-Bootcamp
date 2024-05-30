# W - Fowards
# S - Backwards
# A - Counter-Clockwise
# D - Clockwise
# C - Clear drawing
from turtle import Turtle, Screen

turtle = Turtle()


def forward():
    turtle.forward(10)


def backward():
    turtle.backward(10)


def counter_clockwise():
    turtle.left(45)


def clockwise():
    turtle.right(45)


def clear():
    turtle.clear()
    turtle.home()
    turtle.clear()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
