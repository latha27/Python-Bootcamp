# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:06:41 2022

@author: Jay
"""

for number in range (1,101):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%5==0:
        print("Buzz")
    elif number%3==0:
        print("Fizz")
    else:
        print(number)