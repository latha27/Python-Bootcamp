# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:28:28 2022

@author: Jay
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n1=name1.lower()
n2=name2.lower()
Total=n1.count('t')+n2.count('t')+n1.count('r')+n2.count('r')+n1.count('u')+n2.count('u')+n1.count('e')+n2.count('e')


Total1=n1.count('l')+n2.count('l')+n1.count('o')+n2.count('o')+n1.count('v')+n2.count('v')+n1.count('e')+n2.count('e')


Result=int(str(Total)+str(Total1))

if (Result <10) or (Result>90):
    print(f"Your score is {Result}, you go together like coke and mentos.")

elif (Result >= 40) and (Result <= 50):
    print(f"Your score is {Result}, you are alright together.")

else:
    print(f"Your score is {Result}")




