from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")  # turtle shape
timmy_the_turtle.color("red")  # turtle color
#
# # moving
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(50)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(50)

# square drawing
square_turtle = Turtle()
square_turtle.shape("arrow")
square_turtle.color("green")
square_turtle.forward(50)
square_turtle.right(90)
square_turtle.forward(50)
square_turtle.right(90)
square_turtle.forward(50)
square_turtle.right(90)
square_turtle.forward(50)

screen = Screen()
screen.exitonclick()
