from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        self.score = score
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.clear()
