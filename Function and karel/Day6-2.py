# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:13:50 2022

@author: Jay
"""

def my_function():
    for i in range (0,6):
        move()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
#my_function()
        
        
def turn_left1():        
        turn_left()
        turn_left()
        turn_left()
        
def jump():
    for i in range (0,6):
        move()
        turn_left()
        move()
        turn_left1()
        move()
        turn_left1()
        move()
        turn_left()
jump()