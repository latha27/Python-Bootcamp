def tip_cal():
    print("Welcome to the tip calculator!")
    bill=float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
    num_people= int(input("How many people to split the bill?"))

    cal_each_per_pay = round(float((bill/num_people) * ((tip/100)+1)),2)

    return f"Each person should pay: ${cal_each_per_pay }"
print(tip_cal())