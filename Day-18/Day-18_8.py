import colorgram
import turtle as t
import random
t.colormode(255)
wu = t.Screen()
t.speed("slow")
#color_pt = colorgram.extract('img.jpg', 30)
#first_color = []

#for color in color_pt:
#    r = color.rgb.r
 #   g = color.rgb.g
 #   b = color.rgb.b
#    new_color = (r, g, b)
#    first_color.append(new_color)
#print(first_color)

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
t.setheading(225)
t.penup()
t.forward(360)
t.setheading(0)


def draw_dot():
    for draw in range(0, 20):
        for i in range(0, 20):
            t.position()
            t.dot(15, random.choice(color_list))
            t.penup()
            t.forward(30)
            t.pendown()
        t.left(90)
        t.penup()
        t.forward(30)
        t.left(90)
        t.forward(30)
        for j in range(0, 20):
            t.speed("fastest")
            t.penup()
            t.forward(30)
        t.right(90)
        t.penup()
        t.right(90)
        t.forward(30)


draw_dot()

wu.exitonclick()