# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 23:44:52 2022

@author: Jay
"""

def solution(A):
    # write your code in Python 3.6
    value = numValue([1,0,0,1,1,1])
    if(value < 0):
        ceiling = (value // 2) + 1
    else:
        ceiling = value // 2
    print(ceiling)
    pass

def numValue(bin):
    val = 0
    j = 0
    for i in bin:
        if (i==1):
            val = val + pow(-2, j)
        j = j + 1
    return val

solution("abc")