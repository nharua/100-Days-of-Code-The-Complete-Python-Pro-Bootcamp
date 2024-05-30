from turtle import Turtle, Screen
from random import shuffle, randint

turtle_color = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    "pink",
    "brown",
    "cyan",
    "magenta",
]
shuffle(turtle_color)

all_turtles = []

screen = Screen()
screen.setup(height=500, width=500)
screen.title("TURTLE RACING")
user_bet = screen.textinput(
    title="Make your bet",
    prompt='Which turtle will in the race?\n"red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "cyan", "magenta"\nEnter a color: ',
)
print(user_bet)
y_position = -200

# Instant 10 turles with different color
for color in turtle_color:
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(color)
    my_turtle.penup()
    my_turtle.setposition(x=-200, y=y_position)
    y_position += 45
    all_turtles.append(my_turtle)
if user_bet:
    is_race_on = True
else:
    is_race_on = False

while is_race_on:
    for turtle in all_turtles:
        distance = randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 200:
            if user_bet == turtle.color()[0]:
                print(f"You win")
            else:
                print(f"You lose, Turtle {turtle.color()[0]} is win")
            is_race_on = False

screen.exitonclick()
