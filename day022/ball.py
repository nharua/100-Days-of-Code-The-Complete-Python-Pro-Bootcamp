from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_direction = 1
        self.x_direction = 1
        self.ball_speed = 0.1

    def move(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.y_direction *= -1
        # elif self.ycor() == -290:
        #     self.y_direction = 1
        new_x = self.xcor() + 10 * self.x_direction
        new_y = self.ycor() + 10 * self.y_direction
        self.goto(x=new_x, y=new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.x_direction *= -1
        self.ball_speed = 0.1
