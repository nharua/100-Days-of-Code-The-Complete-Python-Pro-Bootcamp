from turtle import Turtle
from random import randint, choice

COLORS = ["red", "blue", "green", "purple", "yellow", "orange"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        gen_car = randint(1, 5)
        if gen_car == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(x=280, y=randint(-260, 260))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
