import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height,width,cover):
    area=height*width
    num_can=area/cover
    num_cans=math.ceil(num_can)
    print(f"You'll need {num_cans} cans of paint")
#area(test_h=2,test_w=4)
paint_calc(height=test_h,width=test_w,cover=coverage)




