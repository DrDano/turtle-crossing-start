import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# All initializers and screen properties
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title(titlestring="Turtle Crossing")
player = Player()
car = CarManager()
car.hideturtle()
scoreboard = Scoreboard

# TODO create a player that starts at the bottom of the screen and listen for the Up keypress to move the turtle north.
# TODO Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left
#  edge of the screen. No cars should be generated in the top and bottom 50px of the screen
#  (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs.


# All actions of the player that occur before game is over
game_is_on = True
game_loop_counter = 0
game_score = 1
game_speed = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkeypress(fun=player.move, key="Up")
    game_loop_counter += 1
    if game_loop_counter % 6 == 0:
        car.create_cars()
    for unit in car.all_cars:
        if player.distance(x=unit.xcor(), y=unit.ycor()) < 15:
            game_is_on = False
    car.hit_the_gas(game_speed)
    if player.ycor() > 260:
        game_score -= game_loop_counter + 180
        player.sety(y=-250)
        game_speed += 1
    scoreboard()

screen.exitonclick()
