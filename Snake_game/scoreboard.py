from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score={self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_score()



