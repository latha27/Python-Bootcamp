# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:24:50 2022

@author: Jay
"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI=(weight)/(height**2)
change=int(round(BMI,0))

if change < 35:
    if change < 18.5:
        print(f"Your BMI is {change},you are underweight")
    if change > 18.5 and change < 25:
        print(f"Your BMI is {change},you are normal weight")
    if change > 25 and change < 30:
        print(f"Your BMI is {change},you are slightly overweight")
    if change > 30 and change < 35:
        print(f"Your BMI is {change},you are obese")
else:
    print(f"Your BMI is {change},you are clinically obese")