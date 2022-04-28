# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:09:13 2022

@author: Jay
"""

year = int(input("Which year do you want to check? "))


if (year%4)==0:
    if (year%100)==0:
        if (year%500)==0:
            print("leap year")
        else:
            print("Not leap year")
    else:
            print("leap year")
else:
    print("Not leap year")