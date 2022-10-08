from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.score=0
        self.heigher_score=int(open("data.txt").read())
        self.write(f"Score : {self.score} | Heigher score : {self.heigher_score}", False, "center", ("Arial", 14, "normal"))

    def generat_score(self):
        self.score += 1
        if self.heigher_score<=self.score:
            self.heigher_score=self.score

        self.clear()
        self.write(f"Score : {self.score} | Heigher score : {self.heigher_score}",False,"center",("Arial",14,"normal"))
        with open("data.txt", mode="w") as file:
            file.write(f'{self.heigher_score}')



    def reset_score(self):
        self.clear()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score : {self.score} | Heigher score : {self.heigher_score}", False, "center",
                   ("Arial", 14, "normal"))
        with open("data.txt", mode="w") as file:
            file.write(f'{self.heigher_score}')



