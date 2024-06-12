#Anoushka Saha
#Turtle Crossing - Main
#100 Days of Code - Day 23
#May 26th, 2024

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Creating new player
player = Player()

#Car manager object
car_manager = CarManager()

#Move the player up when the "Up" key is pressed
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #Collision detection
    for car in car_manager.all_cars:
       if car.distance(player) < 20:
           game_is_on = False 

screen.exitonclick
