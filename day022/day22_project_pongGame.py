# NOTE: SOLUTION
# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score

# TODO: 1 Create the screen
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)
scoreboard = ScoreBoard()

# TODO: 2 Create and move a paddle

# def paddle_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(y=new_y, x=paddle.xcor())
#
#
# def paddle_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(y=new_y, x=paddle.xcor())
#
#
# screen.listen()
# screen.onkey(paddle_up, "Up")
# screen.onkey(paddle_down, "Down")
# paddle = Turtle(shape="square")
# paddle.color("white")
# paddle.shapesize(stretch_len=1, stretch_wid=5)
# paddle.penup()
# # paddle.goto(x=380, y=0)
# paddle.setposition(x=380, y=0)

# TODO: 3 Create another paddle
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# TODO: 4 Create a ball and make it move
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # TODO: 5 Detect collision with paddle
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 340
        or ball.distance(l_paddle) < 50
        and ball.xcor() < 340
    ):
        ball.x_direction *= -1
        ball.ball_speed *= 0.9
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_lscore()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_rscore()


screen.exitonclick()
