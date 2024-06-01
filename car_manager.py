#Anoushka Saha
#Turtle Crossing - Car Class
#100 Days of Code - Day 23
#May 26th, 2024
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        cars = []

    def create_cars(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=2, stretch_len=1)
        new_car.penup()
        new_car.colour(random.choice(COLORS))
        random_y = random.randint(-250,250)
        new_car.goto(300, random_y)