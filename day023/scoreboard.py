from turtle import Turtle

FONT = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-270, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)

    def increase_level(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=-100, y=0)
        self.write(f"GAVE OVER", font=FONT)
