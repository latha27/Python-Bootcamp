# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:01:08 2022

@author: Jay
"""

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
sum = 0
for i in student_heights: #i -> height
  sum += i
#print(sum)

num_student = 0
for i in student_heights: #i -> number
  num_student += 1
#print(num_student)

avg_height = round(sum/num_student)
print(avg_height)
