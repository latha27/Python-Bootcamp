# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:52:13 2022

@author: Jay
"""
def jump():
    turn_left()
    while wall_on_right():
         move()
    turn_left1()
    move()
    turn_left1()
    while front_is_clear():
         move()
    turn_left()

while not at_goal():
    if wall_in_front():
            jump()
    else:
        move()
