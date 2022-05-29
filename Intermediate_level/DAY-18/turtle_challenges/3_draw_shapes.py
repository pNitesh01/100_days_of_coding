from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("arrow")
tim.color("coral")

screen = Screen()

colormode(255)

def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for side in range(3, 11):
    tim.color(get_color())
    
    angle = 360 / side
    
    for _ in range(side):
        tim.forward(100)
        tim.right(angle)
        
screen.exitonclick()