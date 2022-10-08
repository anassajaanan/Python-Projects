COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
from random import choice,randint

class CarManager():

    def __init__(self):
        self.list_cars=[]
        self.level=0
        self.increment=0



    def add_cars(self):
        random_num=randint(1, 10-self.level)
        if random_num==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.color(choice(COLORS))
            new_car.setheading(180)
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(330, randint(-250, 250))
            self.list_cars.append(new_car)


    def move_care(self):
        for i in range(len(self.list_cars)):
            self.list_cars[i].forward(STARTING_MOVE_DISTANCE+self.increment)
    def speed(self):
        self.level+=1
        self.increment+=3


    def reset_cars(self):
        for car in self.list_cars:
            car.goto(1000,1000)



