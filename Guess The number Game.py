logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
from random import randint
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
guessing_number=randint(0,100)
print("Pssst, the correct answer is ",guessing_number)
difficulty=input("Choose a difficulty. Type 'easy' or 'hard':")
if difficulty.lower()=="easy":
    attempts=10
    print("You have 10 attempts remaining to guess the number.")
    while attempts>0:
        make_guess=int(input("Make a guess:  "))
        attempts-=1
        if attempts==0:
            break
        if make_guess<guessing_number:
            print("Too low.")
            print("Guess again.")
            print("You have ",attempts," attempts remaining to guess the number.")
        elif make_guess>guessing_number:
            print("Too high.")
            print("Guess again.")
            print("You have ", attempts, " attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer was {guessing_number}.")
            break
    if attempts==0:
        print("You've run out of guesses, you lose.")
elif difficulty.lower()=="hard":
    attempts=5
    print("You have 5 attempts remaining to guess the number.")
    while attempts>0:
        make_guess=int(input("Make a guess:  "))
        attempts-=1
        if attempts==0:
            break
        if make_guess<guessing_number:
            print("Too low.")
            print("Guess again.")
            print("You have ",attempts," attempts remaining to guess the number.")
        elif make_guess>guessing_number:
            print("Too high.")
            print("Guess again.")
            print("You have ", attempts, " attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer was {guessing_number}.")
            break
    if attempts==0:
        print("You've run out of guesses, you lose.")



