from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")

screen = Screen()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

tim.pensize(15)
tim.hideturtle()
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))
    
screen.exitonclick()
