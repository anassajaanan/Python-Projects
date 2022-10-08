from turtle import Turtle
LIST_RIGHT_POSITIONS=[(755,40),(755,20),(755,0),(755,-20),(755,-40)]
LIST_LEFT_POSITIONS=[(-760,40),(-760,20),(-760,0),(-760,-20),(-760,-40)]

class Paddle:

    def __init__(self):
        self.list_right_squares=[]
        self.list_left_squares=[]
        self.creat_paddle("right")
        self.creat_paddle("left")


    def creat_paddle(self,alignement):
        if alignement=="right":
            for i in range(5):
                new_square = Turtle()
                new_square.hideturtle()
                new_square.speed(-1)
                new_square.penup()
                new_square.shape("square")
                new_square.color("red")
                new_square.goto(LIST_RIGHT_POSITIONS[i])
                new_square.showturtle()
                self.list_right_squares.append(new_square)
        else:
            for i in range(5):
                new_square = Turtle()
                new_square.hideturtle()
                new_square.speed(-1)
                new_square.penup()
                new_square.shape("square")
                new_square.color("blue")
                new_square.goto(LIST_LEFT_POSITIONS[i])
                new_square.showturtle()
                self.list_left_squares.append(new_square)


    def move_up_r(self):
        if self.list_right_squares[0].ycor()<395:
            for i in range(5):
                self.list_right_squares[i].setheading(90)
                self.list_right_squares[i].forward(50)

    def move_up_l(self):
        if self.list_left_squares[0].ycor() < 395:
            for i in range(5):
                self.list_left_squares[i].setheading(90)
                self.list_left_squares[i].forward(50)

    def move_down_r(self):
        if self.list_right_squares[-1].ycor() > -380:
            for i in range(5):
                self.list_right_squares[i].setheading(270)
                self.list_right_squares[i].forward(50)

    def move_down_l(self):
        if self.list_left_squares[-1].ycor() > -380:
            for i in range(5):
                self.list_left_squares[i].setheading(270)
                self.list_left_squares[i].forward(50)



