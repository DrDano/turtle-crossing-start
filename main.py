import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# All initializers
player = Player()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title(titlestring="Turtle Crossing")

# TODO create a player that starts at the bottom of the screen and listen for the Up keypress to move the turtle north.
# TODO Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left
#  edge of the screen. No cars should be generated in the top and bottom 50px of the screen
#  (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs.

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkeypress(fun=player.move, key="Up")

screen.exitonclick()
