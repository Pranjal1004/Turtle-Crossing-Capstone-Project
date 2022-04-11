from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            car_color = random.randint(0, 5)
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(COLORS[car_color])
            self.all_cars.append(car)
            initial_x = 290
            initial_y = random.randint(-250, 260)
            car.goto(initial_x, initial_y)

    def move(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.speed)

    def inc_speed(self):
        self.speed += MOVE_INCREMENT
