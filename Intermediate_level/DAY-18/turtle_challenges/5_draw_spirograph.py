from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("arrow")

screen = Screen()

colormode(255)

def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
    
tim.speed("fastest")

def draw_spirograph(no_of_circles):
    tilt_angle = 360 / no_of_circles

    for _ in range(no_of_circles):
        current_heading = tim.heading()
        tim.color(get_color())
        tim.circle(100)
        tim.setheading(current_heading + tilt_angle) 

draw_spirograph(100)

screen.exitonclick()