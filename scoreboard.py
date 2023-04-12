from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data_file:
            self.high_score = int(data_file.read())
        self.penup()
        self.color('white')
        self.hideturtle()
        top = (0, 270)
        self.goto(top)
        self.refresh()

    def refresh(self):
        self.clear()
        # self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        # self.write("Score: %s" % self.score, align=ALIGNMENT, font=FONT)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.refresh()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data_file:
                data_file.write(f"{self.high_score}")
        self.score = 0
        self.refresh()
