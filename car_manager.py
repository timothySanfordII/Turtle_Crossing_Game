COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(COLORS[random.randint(0, len(COLORS) - 1)])
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def collision_detect(self, user):
        for car in self.all_cars:
            if car.distance(user) < 22:
                return True

    def level_up(self):
        self.car_speed += MOVE_INCREMENT