# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:24:31 2022

@author: Jay
"""
import random
names_string=input("provide the names:")
names=names_string.split(",")
name_s=len(names)

random_range=random.randint(0,name_s-1)
print(f"{names[random_range]} is going to buy the meal today!")

