from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        self.read_high_score()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.write_high_score()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_high_score(self):
        with open('data.txt', 'r') as file:
            self.high_score = int(file.read())
            
    def write_high_score(self):
        with open('data.txt', 'w') as file:
            file.write(str(self.high_score))