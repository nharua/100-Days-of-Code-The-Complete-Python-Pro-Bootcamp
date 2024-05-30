from turtle import Turtle, Screen

timmy_turtle = Turtle()

for _ in range(20):
    timmy_turtle.forward(10)
    timmy_turtle.penup()
    timmy_turtle.forward(10)
    timmy_turtle.pendown()


my_screen = Screen()
my_screen.exitonclick()
