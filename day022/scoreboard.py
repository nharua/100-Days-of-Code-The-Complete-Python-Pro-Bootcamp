from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 30, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=260)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(x=100, y=260)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def update_rscore(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_lscore(self):
        self.l_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
