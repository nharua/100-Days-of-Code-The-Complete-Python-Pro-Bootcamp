from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(y=new_y, x=self.xcor())

    def down(self):
        new_y = self.ycor() - 20
        self.goto(y=new_y, x=self.xcor())
