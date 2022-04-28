# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:24:12 2022

@author: Jay
"""

print("Welcome to Treasure Island.Your mission is to find out the treasure")
n1=input("left or right?")

if n1=="left":
    n2=input("swim or wait?")
    if n2=="wait":
        n3=input("Which door? Red,Yellow,Blue")
        if n3=="Yellow":
            print("You win")
        else:
            print("Game over")
    else:
        print("Game Over")
else:
    print("Game Over")