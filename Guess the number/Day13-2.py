#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint

def make_guess(user_guess,guess_choice,choose_choice):
    if user_guess > guess_choice:
        print("Too high. Guess again")
        return choose_choice-1
    elif user_guess < guess_choice:
        print ("Too low, Guess again")
        return choose_choice-1
    else:
        return f"You got it! The answer was {guess_choice}"
        

print("Welcome to the number guessing game!")
print("I'm thinking of a number 1 to 100")
guess_choice=randint(1, 100)
choose_choice=input("Choose a difficulty. Type 'easy' or 'hard':")
if choose_choice=="easy":
    choose_choice=10
    

elif choose_choice=="hard":
    choose_choice=5
    
user_guess=0
while user_guess != guess_choice:
    print(f"You have {choose_choice} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    choose_choice = make_guess(user_guess, guess_choice, choose_choice)
    if choose_choice == 0:
      print("You've run out of guesses, you lose.")
    elif user_guess != guess_choice:
      print("Guess again.")

make_guess()