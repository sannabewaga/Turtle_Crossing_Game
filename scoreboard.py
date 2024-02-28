from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()

        self.goto(-280,250)

        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)
    def level_up(self):
        self.level+=1
        self.update_score()

    def game_over(self):
        self.clear()
        self.home()
        self.write(f"GAME OVER, SCORE : {self.level}",align="center",font= FONT)

