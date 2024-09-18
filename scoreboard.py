from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.penup()
        self.goto(-200, 250)
        self.hideturtle()
        self.write(f"level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.color("black")
        self.write("GAME OVER", align="center", font=FONT)

