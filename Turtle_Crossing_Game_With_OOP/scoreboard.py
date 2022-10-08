FONT = ("Times New Roman", 14, "bold")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-240,260)
        self.write(f"Level :  {self.score}", False, "center", FONT )

    def game_over(self):
        self.color("indianred3")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Times New Roman", 60, "bold"))
    def new_score(self):
        self.clear()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-240,260)
        self.write(f"Level :  {self.score}", False, "center", FONT )

