# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:52:25 2022

@author: Jay
"""

def turn_left1():        
        turn_left()
        turn_left()
        turn_left()
        
def jump():
        move()
        turn_left()
        move()
        turn_left1()
        move()
        turn_left1()
        move()
        turn_left()


while not at_goal():
    jump()