from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_cars(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.hideturtle()
        new_car.goto(x=320, y=random.randint(-250, 250))
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.showturtle()
        self.all_cars.append(new_car)

    def hit_the_gas(self, speed_up):
        for car in self.all_cars:
            if speed_up:
                car.backward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT)
            car.backward(STARTING_MOVE_DISTANCE)

