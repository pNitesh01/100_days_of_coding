# STEP 1: Extract color from the image
# STEP 2: Draw the painting

import colorgram, random
from turtle import Turtle, Screen, colormode

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

tim  = Turtle()
tim.speed('fastest')
tim.hideturtle()
tim.penup()
screen = Screen()
colormode(255)

def get_color():
    return random.choice(rgb_colors)

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

num_of_dots = 100  

for dot_count in range(1, num_of_dots + 1):    
    tim.dot(20, get_color())
    tim.forward(50)

    if dot_count%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

    
screen.exitonclick()