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

#Move the player up when the "Up" key is pressed
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
