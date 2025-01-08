import random
from hangman_word import word_list
from LOGO import stages
chosen_word=random.choice(word_list)
#print(f"the chosen word is {chosen_word}")
#####
length= len(chosen_word)
display=[]
for i in range(length):
    display+="_"
print(display)
lives=6
end=False
while not end:
    ask=input("guess a letter:").lower()
    if ask in display:
        print(f"You've already guessed {ask}")
    for i in range(length):
        letter=chosen_word[i]
        if letter==ask:
            display[i]=letter
    if ask not in chosen_word:
        print(f"You've chosen '{ask}' which is wrong ")
        lives-=1
        if lives==0:
            end=True
            print("YOU LOST")
    print(display)
    if "_" not in display:
        end=True
        print("YOU WIN")
    print(stages[lives])