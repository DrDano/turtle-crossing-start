from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=320, y=random.randint(-250, 250))
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1, 3, 2)
        self.showturtle()

    def hit_the_gas(self):
        self.setx(x=self.xcor() - 10)
