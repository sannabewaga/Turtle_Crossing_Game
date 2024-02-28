import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Turtle Crossing Game")

player = Player()
cars_manager = CarManager()
sb = Scoreboard()


screen.onkey(player.up,key="Up")
screen.onkey(player.down,key="Down")






game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars_manager.create_cars()
    cars_manager.move_cars()

    for car in cars_manager.all_cars:

        if car.distance(player)<20:
            sb.game_over()
            game_is_on= False


    if player.ycor()>280:
        player.goto((0, -280))
        cars_manager.increase_speed()
        sb.level_up()




































screen.exitonclick()