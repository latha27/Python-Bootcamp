# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:13:17 2022

@author: Jay
"""
import random
letter=['a','b','c','d']
symbol=['%','*','^']
number=['1','2','3','4','5']
password_list=[]

print("Welcome to password Generator!")
Pass_letter=int(input("How many letters would you like in your password?"))
Pass_sym=int(input("How many symbol would you like?"))
Pass_num=int(input("How many num woukd you like?"))

for char in range (1, Pass_letter+1):
    password_list+=random.choice(letter)
    

for sym in range (1,Pass_sym+1):
    password_list+=random.choice(symbol)


for num in range (1,Pass_num+1):
    password_list+=random.choice(number)


print(password_list)
