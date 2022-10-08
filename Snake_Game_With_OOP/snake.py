from turtle import Turtle
MOVE=20
SPEED=10
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.list_turtles=[]
        self.creat_segments()
        self.head = self.list_turtles[0]


    def creat_segments(self):
        for position in STARTING_POSITION:
            self.add(position)

    def add(self,position):
        if position==(0,0):
            new_turtle = Turtle(shape="classic")
            new_turtle.speed(SPEED)
            new_turtle.color("red")
            new_turtle.penup()
            new_turtle.goto(position)
            self.list_turtles.append(new_turtle)
        else:

            new_turtle = Turtle(shape="circle")
            new_turtle.speed(SPEED)
            new_turtle.color("green")
            new_turtle.penup()
            new_turtle.goto(position)
            self.list_turtles.append(new_turtle)

    def extand(self):
        self.add(self.list_turtles[-1].position())




    def move(self):
        for i in range(len(self.list_turtles)-1 ,0,-1):
            new_x = self.list_turtles[i-1].xcor()
            new_y = self.list_turtles[i-1].ycor()
            self.list_turtles[i].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading()!=180:
            self.list_turtles[0].setheading(0)
    def collision_tail(self):
        for segment in self.list_turtles[1:]:
            if self.head.distance(segment)<10:
                return True

    def reset_snack(self):
        for turtle in self.list_turtles:
            turtle.goto(1000,1000)
        self.list_turtles=[]
        self.creat_segments()
        self.head = self.list_turtles[0]


