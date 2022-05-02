#Step 1:

word_list=["latha","jay"]
import random
chosen_word=random.choice(word_list)
display=[]

for i in range(0,len(chosen_word)):
    display.append("_")
print(display)

for i in range(len(chosen_word)):
    guess=input("Guess a letter:").lower()
    for position in range(0,len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    print(display)
    if "_" not in display:
        print("you Win.")
    

#Step 2:
