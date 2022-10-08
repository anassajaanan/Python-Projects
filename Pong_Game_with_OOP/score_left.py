from turtle import Turtle

class ScoreLeft(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed(-1)
        self.goto(-130, 280)
        self.write(f"{self.score_left}", False, "center", ("Times New Roman", 100, "bold"))

    def add_score_left(self):
        self.clear()
        self.score_left += 1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed(-1)
        self.goto(-130, 280)
        self.write(f"{self.score_left}", False, "center", ("Times New Roman", 100, "bold"))

    def game_over_left(self):
        self.penup()
        self.hideturtle()
        self.color("indianred3")
        self.speed(-1)
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Times New Roman", 100, "bold"))
        self.penup()
        self.hideturtle()
        self.color("indianred3")
        self.speed(-1)
        self.goto(0, -50)
        self.write("The Right player is the winner", False, "center", ("Times New Roman", 40, "normal"))