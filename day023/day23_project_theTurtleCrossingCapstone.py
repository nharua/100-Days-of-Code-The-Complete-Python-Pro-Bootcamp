from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)


# TODO: 1 init the turtle

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    # Detect successful crossing
    if player.ycor() >= 290:
        player.bounce()
        scoreboard.increase_level()
        car_manager.increase_car_speed()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
