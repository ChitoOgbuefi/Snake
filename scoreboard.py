from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.teleport(0, 280)
        self.color("white")
        self.hideturtle()
        with open("high_score.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.update_scoreboard()

    def score_increase(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score:
                high_score.write(str(self.score))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset1(self):

        self.score = 0
        self.update_scoreboard()



