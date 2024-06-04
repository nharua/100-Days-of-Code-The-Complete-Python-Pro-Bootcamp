# NOTE:
# 1 Create a snake body
# 2 Move the snake
# 3 Control the snake
# 4 Detect collision with food
# 5 Create a scoreboard
# 6 Detect collision with wall
# 7 Detect collision with tail

from re import S
from turtle import Screen, Turtle
import time
from scoreboard import ScoreBoard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# TODO: 1 Screen setup and creating snake body

# # make snake body with 3square (20x20pixel) square
# x_pos = 0
# y_pos = 0
# snake_body = []
# for _ in range(3):
#     snake = Turtle(shape="square")
#     snake.color("white")
#     snake.penup()
#     snake.goto(x=x_pos, y=y_pos)
#     x_pos -= 20
#     snake_body.append(snake)
#
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
# TODO:3 Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
# # TODO: 2 Move the snake automatically.
#
game_is_on = True
speed_game = 0.5
while game_is_on:
    screen.update()
    time.sleep(speed_game)
    #     # for seg in snake_body:
    #     #     seg.forward(20)
    #     for seg_num in range(len(snake_body) - 1, 0, -1):
    #         new_x = snake_body[seg_num - 1].xcor()
    #         new_y = snake_body[seg_num - 1].ycor()
    #         snake_body[seg_num].goto(new_x, new_y)
    #     snake_body[0].forward(20)
    snake.move()
    # TODO: 4 Detect collision with Food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        # TODO: 5 Create a scoreboard and update scoreboard
        scoreboard.increase_score()
        snake.extend()
    # TODO: 6 Detect collision with wall
    if (
        snake.snake_head.xcor() > 280
        or snake.snake_head.xcor() < -280
        or snake.snake_head.ycor() > 280
        or snake.snake_head.ycor() < -280
    ):
        game_is_on = False
    # TODO: 7 Detect collision with tail
    # for segment in snake.snake_body:
    #     if segment == snake.snake_head:
    #         pass
    #     elif snake.snake_head.distance(segment) < 10:
    #         game_is_on = False
    # Using slicing in python list
    for segment in snake.snake_body[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False

scoreboard.game_over()

screen.exitonclick()
