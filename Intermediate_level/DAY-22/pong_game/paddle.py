from turtle import Turtle

STEP_SIZE = 20

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)
        
    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + STEP_SIZE)
        
    def move_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - STEP_SIZE)