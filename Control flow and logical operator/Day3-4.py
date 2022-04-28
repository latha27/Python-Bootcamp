# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:34:16 2022

@author: Jay
"""

order_pizza=input("Enter the pizza which you need:")
pepperoni=input("Need to add pepperoni?Y or N:")
extra=input("Need to add extra cheesev?Y or N:")

bill=0

small=15
medium=20
large=25
small_pepperoni=2
medium_Large_pepperoni=3
extra_cheese=1

if order_pizza=="small":    
    if pepperoni=="Y":        
            bill=small+small_pepperoni
    else:
            bill=small
elif order_pizza=="medium":    
    if pepperoni=="Y":        
            bill=medium+medium_Large_pepperoni            
    else:
            bill=medium           
elif order_pizza=="large":
    if pepperoni=="Y":       
            bill=large+medium_Large_pepperoni
    else:
            bill=large

if extra=="Y":
    bill=bill+extra_cheese
    print(bill)
else:
    print(bill)
    