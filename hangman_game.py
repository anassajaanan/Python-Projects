stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

import random
random_nouns=["anasajaan","ajaananan","anasyahya","camel","coco"]
random_string=random.choice(random_nouns)
print(logo)
print(random_string)

empty_list=["_"]*len(random_string)
lives=7
while lives>0:
    char=input("enter a char    ")
    while char in empty_list:
        char = input("you have already guessed, try another one    ")
    if char in random_string:
        for i in range(len(random_string)):
            if random_string[i]==char:
                empty_list[i]=char
        # print(empty_list)
        string="".join(empty_list)
        print(string)
        if random_string == string:
            print("You Win")
            break
    else:
        print(stages[lives - 1])
        lives -= 1
    if lives==0:
        print("you lose")












