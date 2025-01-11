import random
from logo import logo
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    chosen_card=random.choice(cards)
    return chosen_card

def calculate_scores(chosen_card):
    if sum(chosen_card)==21 and len(chosen_card)==2:
        return 0
    if 11 in chosen_card and sum(chosen_card) > 21:
        chosen_card.remove(11)
        chosen_card.append(1)
    return sum(chosen_card)
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "TIED"
    elif user_score==0:
        return "You won with a BLACKJACK."
    elif computer_score==0:
        return "Computer won with a BLACKJACK."
    elif user_score>21:
        return "You lose,You went over."
    elif computer_score>21:
        return "You win,computer went over."
    elif user_score>computer_score:
        return "You win."
    elif computer_score > user_score:
        return "Computer win."
    else:
        return "You lose."


def play_blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over= False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        user_score=calculate_scores(user_cards)
        computer_score=calculate_scores(computer_cards)
        print(f"Your cards:{user_cards}, Current score:{user_score}")
        print(f"Computers cards: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True
        else:
            user_deal=input("Type 'yes' to get a card or type 'no' to exit.\n").lower()
            if user_deal=="yes":
                user_cards.append(deal_card())
            else:
                game_over=True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score=calculate_scores(computer_cards)
    print(f"Your final handd:{user_cards},final score:{user_score} ")
    print(f"Computer's final hand:{computer_cards},final score:{computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play Blackjack? Type 'yes' to play Blackjack or type 'no' to exit.")=="yes":
    os.system('cls')
    play_blackjack()