logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
from random import choice
print(logo)
def play():
    start_game = input("Do you want to play a game of Blackjack Type 'y' or 'n'")
    if start_game == 'n':
        return
    else:
        list_cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]
        user_list_cards=[]
        computer_list_cards=[]
        user_first_card=choice(list_cards)
        if user_first_card==1:
            user_first_card=11
        computer_first_card=choice(list_cards)
        if computer_first_card==1:
            computer_first_card=11
        user_second_card=choice(list_cards)
        if user_second_card==1:
            user_second_card=11
        computer_second_card=choice(list_cards)
        if computer_second_card==1:
            computer_second_card=11
        if user_first_card==11 and user_second_card==11:
            user_first_card=11
            user_second_card=1
        if computer_first_card==11 and computer_second_card==11:
            computer_first_card=11
            computer_second_card=1
        user_list_cards.append(user_first_card)
        user_list_cards.append(user_second_card)
        print(user_list_cards)
        computer_list_cards.append(computer_first_card)
        computer_list_cards.append(computer_second_card)
        print(computer_list_cards)
        if 10 in user_list_cards:
            if 11 in user_list_cards:
                print("Your final hand: ", user_list_cards, " final score:", sum(user_list_cards))
                print("Computer's final hand: ", computer_list_cards, "final score: ", sum(computer_list_cards))
                print("Win with a Blackjack 😎")
                play()
                return
        if 10 in computer_list_cards:
            if 11 in computer_list_cards:
                print("Your final hand: ", user_list_cards, " final score:", sum(user_list_cards))
                print("Computer's final hand: ", computer_list_cards, "final score: ", sum(computer_list_cards))
                print("Lose with a Blackjack 😭")
                play()
                return
        print("Your cards: ",user_list_cards,", current score: ",sum(user_list_cards))
        print("Computer's first card :",computer_first_card)
        if sum(computer_list_cards)==sum(user_list_cards):
            print("Draw 🙃")
            play()
            return
        continue_game=input("Type 'y' to get another card, type 'n' to pass")
        if continue_game=="n":
            if sum(computer_list_cards)<17:
                while sum(computer_list_cards)<17:
                    computer_add_card=choice(list_cards)
                    computer_list_cards.append(computer_add_card)
                    if 11 in computer_list_cards:
                        i= computer_list_cards.index(11)
                        computer_list_cards[i] = 1
                computer_score=sum(computer_list_cards)
                user_score=sum(user_list_cards)
                if computer_score>user_score and computer_score<=21:
                    print("Your final hand: ",user_list_cards," final score:", sum(user_list_cards))
                    print("Computer's final hand: ",computer_list_cards, "final score: ",computer_score)
                    print("You lose 😤")
                    play()
                    return
                else:
                    print("Your final hand: ", user_list_cards, " final score:", sum(user_list_cards))
                    print("Computer's final hand: ",computer_list_cards," final score: ",computer_score)
                    print("Opponent went over. You win 😁")
                    play()
                    return
            else:
                computer_score = sum(computer_list_cards)
                user_score = sum(user_list_cards)
                if computer_score>user_score:
                    print("Your final hand: ", user_list_cards, " final score:", user_score)
                    print("Computer's final hand: ", computer_list_cards, "final score: ", computer_score)
                    print("You lose 😤")
                    play()
                    return
                else:
                    print("Your final hand: ", user_list_cards, " final score:", sum(user_list_cards))
                    print("Computer's final hand: ", computer_list_cards, " final score: ", computer_score)
                    print("Opponent went over. You win 😁")
                    play()
                    return
        while continue_game=="y":
            user_add_card=choice(list_cards)
            if sum(user_list_cards)<=10:
                if user_add_card==1:
                    user_add_card=11
            user_list_cards.append(user_add_card)
            if sum(user_list_cards)>21:
                print("Your final hand: ", user_list_cards, " final score:", sum(user_list_cards))
                print("Computer's final hand: ", computer_list_cards, "final score: ", sum(computer_list_cards))
                print("You lose 😤")
                play()
                return
            while sum(computer_list_cards)<17:
                computer_add_card=choice(list_cards)
                computer_list_cards.append(computer_add_card)
            computer_score = sum(computer_list_cards)
            user_score = sum(user_list_cards)
            if computer_score>21:
                print("Your final hand: ", user_list_cards, " final score:", sum(user_list_cards))
                print("Computer's final hand: ", computer_list_cards, "final score: ", computer_score)
                print("You win 😁")
                play()
                return
            if user_score==21 and computer_score<21:
                print("Your final hand: ", user_list_cards, " final score:", sum(user_list_cards))
                print("Computer's final hand: ", computer_list_cards, "final score: ", computer_score)
                print("You win 😁")
                play()
                return
            print("Your cards: ", user_list_cards, ", current score: ", sum(user_list_cards))
            print("Computer's first card :", computer_first_card)
            continue_game = input("Type 'y' to get another card, type 'n' to pass")
            if continue_game=="n":
                if user_score>21:
                    print("Your final hand: ", user_list_cards, " final score:", user_score)
                    print("Computer's final hand: ", computer_list_cards, "final score: ", computer_score)
                    print("You lose 😤")
                    play()
                    return
                elif computer_score>user_score:
                    print("Your final hand: ", user_list_cards, " final score:", user_score)
                    print("Computer's final hand: ", computer_list_cards, "final score: ", computer_score)
                    print("You lose 😤")
                    play()
                    return
                elif computer_score==user_score:
                    print("Your cards: ", user_list_cards, ", current score: ", sum(user_list_cards))
                    print("Computer's cards: ", computer_list_cards, "current score: ", sum(computer_list_cards))
                    print("Draw 🙃")
                    play()
                    return
                else:
                    print("Your final hand: ", user_list_cards, " final score:", sum(user_list_cards))
                    print("Computer's final hand: ", computer_list_cards, " final score: ", computer_score)
                    print("Opponent went over. You win 😁")
                    play()
                    return
print(play())


