import colorgram
import turtle as t
import random


t.colormode(255)
wu = t.Screen()
#first_color = []
#color_extract = colorgram.extract('img1.jpg', 20)
#print(color_extract)
#for color in color_extract:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    first_color.append(new_color)
#print(first_color)

color_list = [(226, 229, 235), (244, 237, 222), (243, 234, 240), (232, 242, 237), (192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26), (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127)]
#for i in range(20):
t.dot(10, random.choice(color_list))
t.penup()
t.forward(30)
t.pendown()
t.dot(10, random.choice(color_list))
t.left(120)
t.penup()
t.forward(30)
t.dot(10, random.choice(color_list))
t.penup()
t.left(60)
t.forward(30)
t.pendown()
t.dot(10, random.choice(color_list))
t.penup()
t.left(60)
t.forward(30)
t.pendown()
t.dot(10, random.choice(color_list))
t.penup()
t.left(60)
t.forward(30)
t.pendown()
t.dot(10, random.choice(color_list))
t.penup()
t.left(60)
t.forward(30)
t.pendown()
t.dot(10, random.choice(color_list))


t.penup()
t.left(60)
t.forward(30)


t.right(60)

t.penup()
t.forward(30)
t.pendown()
t.dot(10, random.choice(color_list))
t.left(120)
t.penup()
t.forward(30)
t.dot(10, random.choice(color_list))
t.penup()
t.forward(30)
t.dot(10, random.choice(color_list))
t.penup()
t.left(60)
t.forward(30)
t.dot(10, random.choice(color_list))
t.forward(30)
t.dot(10, random.choice(color_list))
t.left(60)
t.penup()
t.forward(30)
t.dot(10, random.choice(color_list))











wu.exitonclick()