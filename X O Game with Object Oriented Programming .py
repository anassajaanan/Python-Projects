from random import choice
class Game:
    def __init__(self):
        self.row1=["⬜️", "⬜️", "⬜️"]
        self.row2=["⬜️", "⬜️", "⬜️"]
        self.row3=["⬜️", "⬜️", "⬜️"]
        self.map=[self.row1, self.row2, self.row3]
        self.user_choices=[]
        self.computer_choices=[]
        self.user_input=""
        self.computer_input=""
        self.available_positions=["11","12","13","21","22","23","31","32","33"]
    def generate_position(self):
        # print("\n")
        self.user_input=input("Where do you want to put the treasure? ")
        while self.user_input not in self.user_choices and self.user_input not in self.computer_choices:
            self.user_choices.append(self.user_input)
            self.available_positions.remove(self.user_input)
        self.computer_input=choice(self.available_positions)

        self.computer_choices.append(self.computer_input)
        self.available_positions.remove(self.computer_input)
    def replace_in_map(self):
        choice_user=self.user_input
        choice_computer=self.computer_input
        # self.track += 1
        vertical_u=int(choice_user[1])-1
        horizontal_u=int(choice_user[0])-1
        vertical_c=int(choice_computer[1])-1
        horizontal_c=int(choice_computer[0])-1

        self.map[vertical_u][horizontal_u] = "❌️"
        print("----------------------------------")
        print(f"{self.row1}\n{self.row2}\n{self.row3}")
        print("\n")
        if  not self.cheak_winner_user():

            print("Let me think...!! 🤔🤔🤔")
            print("\n")
            self.map[vertical_c][horizontal_c] = "🔴  "
            print(f"{self.row1}\n{self.row2}\n{self.row3}")
            print("----------------------------------")



    def cheak_winner_user(self):
        if all(x in self.user_choices for x in ["11","21","31"]):
            print("You're the Winner, Gongratulation!!  🎉🎉🎉🎉🎉🎉")
            return True
        if all(x in self.user_choices for x in ["12","22","32"]):
            print("You're the Winner, Gongratulation!!  🎉🎉🎉🎉🎉🎉🎉")
            return True
        if all(x in self.user_choices for x in ["13","23","33"]):
            print("You're the Winner, Gongratulation!!  🎉🎉🎉🎉🎉🎉")
            return True
        if all(x in self.user_choices for x in ["11","12","13"]):
            print("You're the Winner, Gongratulation!!  🎉🎉🎉🎉🎉🎉🎉")
            return True
        if all(x in self.user_choices for x in ["21","22","23"]):
            print("You're the Winner, Gongratulation!! 🎉🎉🎉🎉🎉🎉🎉🎉")
            return True
        if all(x in self.user_choices for x in ["31","32","33"]):
            print("You're the Winner, Gongratulation!!  🎉🎉🎉🎉🎉🎉🎉🎉")
            return True
        if all(x in self.user_choices for x in ["11","22","33"]):
            print("You're the Winner, Gongratulation!!  🎉🎉🎉🎉🎉🎉🎉🎉")
            return True
        if all(x in self.user_choices for x in ["13","22","31"]):
            print("You're the Winner, Gongratulation!!  🎉🎉🎉🎉🎉🎉🎉🎉🎉")
            return True
        return False
    def cheak_winner_computer(self):
        if all(x in self.computer_choices for x in ["11","21","31"]):
            print("You lose 🤪🤪🤪🤪🤪🤪🤪")
            return True
        if all(x in self.computer_choices for x in ["12","22","32"]):
            print("You lose 🤪🤪🤪🤪🤪🤪🤪")
            return True
        if all(x in self.computer_choices for x in ["13","23","33"]):
            print("You lose 🤪🤪🤪🤪🤪🤪🤪")
            return True
        if all(x in self.computer_choices for x in ["11","12","13"]):
            print("You lose 🤪🤪🤪🤪🤪🤪🤪")
            return True
        if all(x in self.computer_choices for x in ["21","22","23"]):
            print("You lose 🤪🤪🤪🤪🤪🤪🤪")
            return True
        if all(x in self.computer_choices for x in ["31","32","33"]):
            print("You lose 🤪🤪🤪🤪🤪🤪🤪")
            return True
        if all(x in self.computer_choices for x in ["11","22","33"]):
            print("You lose 🤪🤪🤪🤪🤪🤪🤪🤪")
            return True
        if all(x in self.computer_choices for x in ["13","22","31"]):
            print("You lose 🤪🤪🤪🤪🤪🤪🤪🤪")
            return True
        return False

    def should_continue(self):
        # if len(self.available_positions) != 0:
            if  self.cheak_winner_user() or  self.cheak_winner_computer():
                return False
            return True


# from game_project import Game
game=Game()
print(f"{game.row1}\n{game.row2}\n{game.row3}")
while game.should_continue():
        game.generate_position()
        game.replace_in_map()








