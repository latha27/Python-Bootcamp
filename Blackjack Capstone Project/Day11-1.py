import random
user_cards=[]
computer_cards=[]
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    for i in range(0,2):
        user_cards1=random.choice(cards)
        compute_cards1=random.choice(cards)
        user_cards.append(user_cards1)
        computer_cards.append(compute_cards1)
    print("user_cards:" ,user_cards)
    print("computer_cards:" ,computer_cards)

deal_card()

def calculate_score():
    cal_user_score=0
    cal_computer_score=0
    for num in user_cards:
        cal_user_score=cal_user_score+num
    if user_cards[0]==11 and user_cards[1]==10 or user_cards[0]==10 and user_cards[1]==11:
        print("User count is 0")
    elif user_cards[0]==11 and cal_user_score > 21 or user_cards[1]==11 and cal_user_score > 21:
        print("User count is :",cal_user_score-10)
    else:
        print("User count:",cal_user_score)
    

    for num in computer_cards:
        cal_computer_score=cal_computer_score+num
    if computer_cards[0]==11 and computer_cards[1]==10 or computer_cards[0]==10 and computer_cards[1]==11:
        print("Computer count is 0")
    elif computer_cards[0]==11 and cal_computer_score > 21 or computer_cards[1]==11 and cal_computer_score  > 21:
        print("User count is :",cal_computer_score-10)
    else:
        print("Computer count:",cal_computer_score)
calculate_score()

if 
   

