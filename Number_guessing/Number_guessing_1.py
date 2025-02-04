import random
import math

number=random.randint(1,100)
easy_hard=input("Easy or Hard:\n").lower()

easy=5
hard=10
if easy_hard=="Easy":
    game_mode=easy
elif easy_hard=="Hard":
    game_mode=hard

def Easy():

    for i in range(easy):
        guess=int(input(("Chose a number:")))
        if guess==number:
            print("You win! You got the right number")
        elif guess>number:
            print("Too High")
        else :
            print("Too low")
def Hard():

    for i in range(hard):
        guess=int(input(("Chose a number:")))
        if guess==number:
            print("You win! You got the right number")
        elif guess>number:
            print("Too High")
        else:
            print("Too low")
if easy_hard=="Easy".lower():
    Easy()
elif easy_hard=="Hard".lower():
    Hard()