# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:17:26 2022

@author: Jay
"""

def turn_left1():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_left1()
    move()
    turn_left1()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()