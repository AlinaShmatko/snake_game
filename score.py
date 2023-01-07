from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("hight_score.txt") as HS:
            self.high_score = HS.read()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def level_up(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score {self.high_score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("hight_score.txt", mode="w") as HS:
                HS.write(f"{self.score}")
        self.score = 0
        self.update()
