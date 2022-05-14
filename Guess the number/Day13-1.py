#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

def make_guess():
    for i in range(choose_choice):
        user_guess=int(input("Make a guess:"))
        if user_guess > guess_choice:
            return "Too high. Guess again"
        elif user_guess < guess_choice:
            return "Too low, Guess again"
    print(f"you have {choose_choice} attempts ramaining to guess the number.")
    return f"You got it! The answer was {guess_choice}"
        
guess_choice=random.randint(1, 100)
print("Welcome to the number guessing game!")
print("I'm thinking of a number 1 to 100")
choose_choice=input("Choose a difficulty. Type 'easy' or 'hard':")
if choose_choice=="easy":
    choose_choice=10
    print("you have 10 attempts ramaining to guess the number.")

elif choose_choice=="hard":
    choose_choice=5
    print("you have 5 attempts ramaining to guess the number.")

print(make_guess())