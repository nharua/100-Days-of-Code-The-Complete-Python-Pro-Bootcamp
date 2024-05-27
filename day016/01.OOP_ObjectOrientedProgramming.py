"""
Classes
    
Objects

Attributes
"""

import turtle

timmy = turtle.Turtle()  # timmy is Object that initiate from Turtle class.
# print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)


screen = turtle.Screen()
# print(screen.canvheight)
screen.setup(width=300, height=300)
screen.exitonclick()
