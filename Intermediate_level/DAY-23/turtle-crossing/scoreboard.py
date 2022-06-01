from turtle import Turtle

ALIGNMENT_LEFT = 'left'
ALIGNMENT_CENTER = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=250)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT_LEFT, font=FONT)
            
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER!", align=ALIGNMENT_CENTER, font=FONT)