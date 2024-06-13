# Anoushka Saha
# Turtle Crossing - Car Class
# 100 Days of Code - Day 23
# May 26th, 2024

from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange"]))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 10

    def finish(self):
       if self.ycor() > 280:
           return True
       else:
           return False
    
    def go_to_start(self):
        self.goto(0,-280)